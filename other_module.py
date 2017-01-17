import logging


def add(x, y):
    """
    Add two items together.
    :param x:
    :param y:
    :return:
    """
    logging.info("added %s and %s to get %s" % (x, y, x+y))

    return x + y
