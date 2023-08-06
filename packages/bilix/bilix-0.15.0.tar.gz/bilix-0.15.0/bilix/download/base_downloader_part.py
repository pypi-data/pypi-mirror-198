import asyncio
from typing import Union, List, Iterable, Tuple
import aiofiles
import httpx
import random
import os
import cgi

from bilix.handle import Handler
from bilix.download.base_downloader import BaseDownloader
from bilix.utils import req_retry, merge_files
from bilix.log import logger


class BaseDownloaderPart(BaseDownloader):
    def __init__(self, client: httpx.AsyncClient = None, videos_dir: str = 'videos',
                 video_concurrency: Union[int, asyncio.Semaphore] = 3, part_concurrency: int = 10,
                 stream_retry=5, speed_limit: Union[float, int] = None, progress=None, browser: str = None):
        """
        Base Async http Content-Range Downloader

        :param client:
        :param browser:
        :param videos_dir:
        :param part_concurrency:
        :param speed_limit:
        :param progress:
        """
        super(BaseDownloaderPart, self).__init__(client, videos_dir, video_concurrency, part_concurrency,
                                                 browser=browser,
                                                 stream_retry=stream_retry, speed_limit=speed_limit, progress=progress)

    async def _pre_req(self, urls: List[Union[str, httpx.URL]]) -> Tuple[int, str]:
        # use GET instead of HEAD due to 404 bug https://github.com/HFrost0/bilix/issues/16
        res = await req_retry(self.client, urls[0], follow_redirects=True, headers={'Range': 'bytes=0-1'})
        total = int(res.headers['Content-Range'].split('/')[-1])
        # get filename
        if content_disposition := res.headers.get('Content-Disposition', None):
            key, pdict = cgi.parse_header(content_disposition)
            filename = pdict.get('filename', '')
        else:
            filename = ''
        # change origin url to redirected position to avoid twice redirect
        if res.history:
            urls[0] = res.url
        return total, filename

    async def get_file(self, url_or_urls: Union[str, Iterable[str]],
                       file_name: str = None, task_id=None, hierarchy: str = '') -> str:
        """

        :param url_or_urls: file url or urls with backups
        :param file_name:
        :param task_id: if not provided, a new progress task will be created
        :param hierarchy:
        :return: downloaded file path
        """
        urls = [url_or_urls] if isinstance(url_or_urls, str) else [url for url in url_or_urls]
        file_dir = f'{self.videos_dir}/{hierarchy}' if hierarchy else self.videos_dir

        if file_name and os.path.exists(f'{file_dir}/{file_name}'):
            logger.info(f'[green]已存在[/green] {file_name}')
            return f'{file_dir}/{file_name}'

        total, req_filename = await self._pre_req(urls)

        if not file_name:
            file_name = req_filename if req_filename else str(urls[0]).split('/')[-1].split('?')[0]
        file_path = f'{file_dir}/{file_name}'
        if os.path.exists(file_path):
            logger.info(f'[green]已存在[/green] {file_name}')
            return file_path

        if task_id is not None:
            await self.progress.update(task_id, total=self.progress.tasks[task_id].total + total, visible=True)
        else:
            task_id = await self.progress.add_task(description=file_name, total=total, visible=True)
        part_length = total // self.part_concurrency
        cors = []
        part_names = []
        for i in range(self.part_concurrency):
            start = i * part_length
            end = (i + 1) * part_length - 1 if i < self.part_concurrency - 1 else total - 1
            part_name = f'{file_name}-{start}-{end}'
            part_names.append(part_name)
            cors.append(self._get_file_part(urls, part_name, task_id, hierarchy=hierarchy))
        file_list = await asyncio.gather(*cors)
        await merge_files(file_list, new_path=file_path)
        if self.progress.tasks[task_id].finished:
            await self.progress.update(task_id, visible=False)
            logger.info(f"[cyan]已完成[/cyan] {file_name}")
        return file_path

    async def _get_file_part(self, urls: List[Union[str, httpx.URL]],
                             part_name, task_id, times=0, hierarchy: str = ''):
        file_dir = f'{self.videos_dir}/{hierarchy}' if hierarchy else self.videos_dir
        if times > self.stream_retry:
            raise Exception(f'STREAM 超过重试次数 {part_name}')
        start, end = map(int, part_name.split('-')[-2:])
        file_path = f'{file_dir}/{part_name}'
        if os.path.exists(file_path):
            downloaded = os.path.getsize(file_path)
            start += downloaded
            if times == 0:
                await self.progress.update(task_id, advance=downloaded)
        if start > end:
            return file_path  # skip already finished
        url_idx = random.randint(0, len(urls) - 1)
        try:
            async with self.client.stream("GET", urls[url_idx], follow_redirects=True,
                                          headers={'Range': f'bytes={start}-{end}'}) as r, self._stream_context(times):
                r.raise_for_status()
                if r.history:  # avoid twice redirect
                    urls[url_idx] = r.url
                async with aiofiles.open(file_path, 'ab') as f:
                    async for chunk in r.aiter_bytes(chunk_size=self.chunk_size):
                        await f.write(chunk)
                        await self.progress.update(task_id, advance=len(chunk))
                        await self._check_speed(len(chunk))
        except (httpx.TransportError, httpx.HTTPStatusError):
            await self._get_file_part(urls, part_name, task_id, times=times + 1, hierarchy=hierarchy)
        return file_path


@Handler.register(name="Part")
def handle(kwargs):
    method = kwargs['method']
    if method == 'f' or method == 'get_file':
        videos_dir = kwargs['videos_dir']
        part_concurrency = kwargs['part_concurrency']
        speed_limit = kwargs['speed_limit']
        d = BaseDownloaderPart(videos_dir=videos_dir, part_concurrency=part_concurrency,
                               speed_limit=speed_limit)
        cors = []
        for key in kwargs['keys']:
            cors.append(d.get_file(key))
        return d, asyncio.gather(*cors)
