import logging

# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")
# logging has default logging-level to warning and above, so we dont see DEBUG and INFO messages by doing the above

# logging.basicConfig(level=logging.DEBUG) # By doing this the logging-level is set to DEBUG and above
# logging.debug("This is a debug message")
# logging.info("This is a info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

logging.basicConfig(level=logging.DEBUG, filename='data_log.log', filemode='w', format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")