import json


def read_login_data():

    with open("data/login_data.json") as file:
        return json.load(file)