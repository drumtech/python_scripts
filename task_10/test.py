### Give two arguments for this script, first - number of entries in the log, second - delay time between writing strings of log

import sys
import os
import logging
import time

logging.basicConfig(filename=f'{time.strftime("%d-%m-%Y---%H:%M:%S")}.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)
a = int(sys.argv[1])
b = int(sys.argv[2])

count = 0
for key,value in os.environ.items():
    if count < a:
        count += 1
        logging.info(f'{key} -> {value}')
        time.sleep(b)
