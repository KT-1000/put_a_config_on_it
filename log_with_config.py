import logging
import logging.config
import other_module


def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    :return:
    """
    logging.config.fileConfig("config.ini")
    logger = logging.getLogger("exampleApp")

    logger.info("Program started")
    result = other_module.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()
