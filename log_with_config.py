import logging
import logging.config
import other_module


def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    :return:
    """
    dictLogConfig = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": "config.log"
            }
        },
        "loggers": {
            "exampleApp": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("exampleApp")

    logger.info("Program started")
    result = other_module.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()
