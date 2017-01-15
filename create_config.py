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
    config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

    with open(file_path, "w") as config_file:
        config.write(config_file)


def get_config(file_path):
    """
    Get a config object.
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


def update_setting(file_path, section, setting, value):
    """
    Update a config setting.
    :param file_path:
    :param section:
    :param setting:
    :param value:
    :return:
    """
    config = get_config(file_path)
    config.set(section, setting, value)
    with open(file_path, "w") as config_file:
        config.write(config_file)


def delete_setting(file_path, section, setting):
    """
    Delete a config setting.
    :param file_path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(file_path)
    config.remove_option(section, setting)
    with open(file_path, "w") as config_file:
        config.write(config_file)


def interpolation_demo(file_path):
    """
    Interpolation means we can use some options to build another option.
    Example would be the font_info option values that can be changed via dictionary.
    :param file_path:
    :return:
    """
    if not os.path.exists(file_path):
        create_config(file_path)

    config = configparser.ConfigParser()
    config.read(file_path)

    print(config.get("Settings", "font_info"))

    print(config.get("Settings", "font_info",
                     vars={"font": "Arial", "font_size": "100"}))

if __name__ == "__main__":
    path = "settings.ini"
    # create_config(path)
    # font = get_setting(path, 'Settings', 'font')
    # font_size = get_setting(path, 'Settings', 'font_size')
    #
    # update_setting(path, "Settings", "font_size", "12")
    #
    # delete_setting(path, "Settings", "font_style")
    interpolation_demo(path)
