import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('rotating_filter')
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler('rotating.log', maxBytes=200*1024, backupCount=3)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('These logs will rotate automatically')