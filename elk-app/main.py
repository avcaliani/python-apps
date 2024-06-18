#!/usr/bin/env python3
# @script   main.py
# @author   Anthony Vilarim Caliani
# @contact  github.com/avcaliani
#
# @description
# Mock script to create random logs...
#
# @usage
# ./main.py
import logging
import random
from datetime import datetime
from time import sleep

HEART = '\033[1;35m❤\033[00m'
CHOICES = ['INFO', 'WARNING', 'ERROR', 'CRITICAL']


def init_log():
    curr_time = datetime.now().strftime('%Y%m%d-%H%M%S')
    logging.basicConfig(
        filename=f'/opt/logs/py-app/py-app.{curr_time}.log',
        filemode='a',
        format='%(asctime)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


if __name__ == '__main__':
    init_log()
    print('Press [Ctrl + c] to stop!')

    while True:
        value = random.choice(CHOICES)
        if value == 'INFO':
            logging.info('We are good!')
        elif value == 'WARNING':
            logging.warning('Ops! Keep your eyes oppened!')
        elif value == 'ERROR':
            logging.error('Houston, we have a problem!')
        else:
            logging.critical('That\'s it... Things are definitely not good!')

        print(datetime.now().strftime(
            f'Last {HEART} heart beat at %Y-%m-%d %H:%M:%S'
        ))
        sleep(1)
