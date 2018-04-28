import time
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logger.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

def error_function():
    raise Exception('Error info')

while True:
    logger.info('Logger info msg')
    try:
        error_function()
    except:
        logger.exception("Some exception occure")
    time.sleep(10)





