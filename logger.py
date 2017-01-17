import logging
import other_module


def main():
    """
    The main entry point of the application.
    :return:
    """
    # add filemode="w" to overwrite
    logging.basicConfig(filename="sample.log",
                        level=logging.INFO)
    logging.info("Program started")
    result = other_module.add(7, 8)
    logging.info("Done!")

if __name__ == "__main__":
    main()
