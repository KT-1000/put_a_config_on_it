import configparser
import os


def create_config(file_path):
    """
    Create a config file.
    :param file_path:
    :return:
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_sizes)s pt")

    with open(file_path, "w") as config_file:
        config.write(config_file)


def get_config(file_path):
    """
    Get a config object
    :param file_path:
    :return config: Config obj
    """
    if not os.path.exists(file_path):
        create_config(file_path)

    config = configparser.ConfigParser()
    config.read(path)

    return config


def get_setting(file_path, section, setting):
    """
    Print a setting to console.
    :param file_path:
    :param section:
    :param setting:
    :return value:
    """
    config = get_config(file_path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}". format(section=section,
                                                   setting=setting,
                                                   value=value)
    print(msg)
    return value

if __name__ == "__main__":
    path = "settings.ini"
    # create_config(path)
    font = get_setting(path, 'Settings', 'font')
    font_size = get_setting(path, 'Settings', 'font_size')
