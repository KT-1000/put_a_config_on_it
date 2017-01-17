import logging

module_logger = logging.getLogger("exampleApp.other_module")


def add(x, y):
    """
    Add two items together.
    :param x:
    :param y:
    :return:
    """
    logger = logging.getLogger("exampleApp.other_module.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))

    return x + y
