import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

def setup_logger():
    Path('logs').mkdir(exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = TimedRotatingFileHandler(
        filename='logs/calculator.log',
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


