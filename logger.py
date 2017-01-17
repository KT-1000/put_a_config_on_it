import logging
import math


def main():
    """
    The main entry point of the application.
    :return:
    """
    # add filemode="w" to overwrite
    logging.basicConfig(filename="sample.log",
                        level=logging.INFO)
    logging.info("Program started")
    result = math.fsum([7, 8])
    logging.info("Done!")

    # log = logging.getLogger("ex")
    #
    # try:
    #     raise RuntimeError
    # except RuntimeError:
    #     log.exception("Error!")
    #
    #     logging.debug("This is a debug message.")
    #     logging.info("Informational message.")
    #     logging.error("An error has occurred!")

if __name__=="__main__":
    main()
