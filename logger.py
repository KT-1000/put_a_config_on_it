import logging
import other_module


def main():
    """
    The main entry point of the application.
    :return:
    """
    logger = logging.getLogger("example_app")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("new.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = other_module.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()
