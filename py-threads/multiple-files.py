#!/usr/bin/env python3
import logging as log
from concurrent.futures import ThreadPoolExecutor
from random import choice

import utils


def main(*pkg_versions):
    main_thread = utils.thread_label('main', utils.RED)
    log.info(f'{main_thread} Creating threads...')
    with ThreadPoolExecutor(max_workers=4) as executor:
        for index in range(len(pkg_versions)):
            color = choice(utils.COLORS)
            utils.COLORS.remove(color)
            executor.submit(
                utils.download_file,
                index,
                pkg_versions[index],
                color
            )
    log.info(f'{main_thread} Done!')


if __name__ == '__main__':
    utils.init_logs()
    main('2.4.0', '3.0.0', '3.0.1', '3.1.2')
