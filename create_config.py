import configparser


def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_sizes)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    path = "settings.ini"
    create_config(path)
