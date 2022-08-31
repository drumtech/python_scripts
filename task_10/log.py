### Just for test, you can change level, than less trigger level than more log you get
import logging
logging.basicConfig(filename='log_file.log', format='%(asctime)s  %(levelname)s  %(message)s', datefmt='%b %d %H:%M:%S', level=logging.DEBUG)
logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning! Something happened!')
logging.error('Error!')
logging.critical('Critical error!!!')
