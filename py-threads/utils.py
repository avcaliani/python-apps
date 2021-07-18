#!/usr/bin/env python3
import logging as log
import os
from time import time
from urllib.error import HTTPError

import wget

# If true, the threads will be executed in background and
# the program will exit.
RUN_AS_DAEMON = False

# If true, the "main" thread will wait all other threads
# to be finished.
WAIT_THREADS = False

# Colors
RED = 31
COLORS = [
    32,  # Green
    33,  # Yellow
    35,  # Magenta
    36,  # Cyan
]


def __url(pkg_version):
    return f'https://archive.apache.org/dist/spark/spark-{pkg_version}/spark-{pkg_version}-bin-hadoop3.2.tgz'


def thread_label(name, color):
    return f'\033[1;{color}m[{name}]\033[00m'


def download_file(id, pkg_version, color):
    thread_name = thread_label(f'{id}_{pkg_version}', color)
    file_name = f'spark-{pkg_version}.tgz'
    file_path = 'dist'
    file_url = __url(pkg_version)
    start_time = time()

    log.info(f'{thread_name} Starting download... URL -> {file_url}')
    os.makedirs(file_path, exist_ok=True)
    try:
        file = wget.download(
            file_url,
            out=f'{file_path}/{file_name}',
            bar=None
        )
        log.info(f'{thread_name} Download finished! File saved at "{file}"')
    except HTTPError as ex:
        log.error(f'{thread_name} ERROR! Desc: {ex}')
    finally:
        hours, rest = divmod(time() - start_time, 3600)
        minutes, seconds = divmod(rest, 60)
        log.info(f'{thread_name} Time elapsed -> {int(hours)}h {int(minutes)}m {int(seconds)}s')


def init_logs():
    log.basicConfig(
        format='\033[1;34m[%(asctime)s]\033[00m %(message)s',
        level=log.INFO,
        datefmt='%H:%M:%S'
    )
