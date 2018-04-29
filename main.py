import time
import datetime

# class OneLineExceptionFormatter(logging.Formatter):
#     def format(self, record):
#         result = super().format(record)
#         if record.exc_text:
#             result = result.replace("\n", " | ")
#         return result

import logging
import logging.config

# Say i have saved my configuration under ./myconf.conf
logging.config.fileConfig('logging_conf.conf')
logger = logging.getLogger(__name__)


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('logger_new.log')
fh.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter = OneLineExceptionFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

logger.addHandler(fh)
# logger.addHandler(ch)

def error_function():
    raise Exception('Error info')

while True:
    logger.info('Logger info msg '+str(datetime.datetime.now()))
    logger.debug('Logger info debug '+str(datetime.datetime.now()))
    logger.info('Some extra value msg before', extra={'extra_key':'before'})
    try:
        error_function()
    except:
        logger.exception("Some exception occure")
    time.sleep(10)
    logger.info('Some extra value msg after', extra={'extra_key':'after'})





