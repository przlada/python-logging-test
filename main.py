import time
import datetime
import logging

class OneLineExceptionFormatter(logging.Formatter):
    # def formatException(self, exc_info):
    #     result = super().formatException(exc_info)
    #     return repr(result)
 
    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", " | ")
        return result


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logger.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = OneLineExceptionFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

def error_function():
    raise Exception('Error info')

while True:
    logger.info('Logger info msg '+str(datetime.datetime.now()))
    logger.debug('Logger info debug '+str(datetime.datetime.now()))
    try:
        error_function()
    except:
        logger.exception("Some exception occure")
    time.sleep(10)





