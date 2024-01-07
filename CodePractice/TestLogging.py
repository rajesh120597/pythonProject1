import logging


# Logging means - You can add logs to the Failure, Information, Error
# Warning to the Users

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("Information logs")
    LOGGER.warning("This is warning logs")
    LOGGER.error("This is error logs")
    LOGGER.critical("This is critical log")


test_print_logs()
