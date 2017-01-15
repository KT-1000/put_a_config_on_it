import configparser
import os


def create_config(file_path):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_sizes)s pt")

    with open(file_path, "w") as config_file:
        config.write(config_file)


def crud_config(file_path):
    """
    Create, read, update or delete a config file.
    :param file_path:
    :return:
    """
    if not os.path.exists(file_path):
        create_config(file_path)

    config = configparser.ConfigParser()
    config.read(file_path)

    # read some values from the config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # change a vlue in the config
    config.set("Settings", "font_size", "12")

    # delete a value from the config
    config.remove_option("Settings", "font_style")

    # write changes back to config
    with open(file_path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "settings.ini"
    # create_config(path)
    crud_config(path)
