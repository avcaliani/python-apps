#!/usr/bin/env python3
import logging as log
from random import choice
from threading import Thread

import utils

# If true, the threads will be executed in background and
# the program will exit.
RUN_AS_DAEMON = False

# If true, the "main" thread will wait all other threads
# to be finished.
WAIT_THREADS = False


def main(pkg_version):
    main_thread = utils.thread_label('main', utils.RED)
    log.info(f'{main_thread} Creating threads...')

    sub_thread = Thread(
        target=utils.download_file,
        args=(1, pkg_version, choice(utils.COLORS)),
        daemon=RUN_AS_DAEMON
    )
    log.info(f'{main_thread} Ready? Go!')
    sub_thread.start()

    flag = "yes" if WAIT_THREADS else "no"
    log.info(f'{main_thread} Wait for the thread to finish? [{flag}]')
    if WAIT_THREADS:
        sub_thread.join()

    log.info(f'{main_thread} Done!')


if __name__ == '__main__':
    utils.init_logs()
    main('3.0.1')
