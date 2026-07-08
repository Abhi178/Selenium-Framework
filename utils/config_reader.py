import configparser

config = configparser.ConfigParser()

config.read("config/config.ini")

BASE_URL = config["DEFAULT"]["base_url"]