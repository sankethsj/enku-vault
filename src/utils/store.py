import platformdirs
import json
import os
import pathlib

global app_data


app_data_path = platformdirs.user_data_path(appname="enku-vault")
os.makedirs(str(app_data_path), exist_ok=True)

JSON_FILENAME = "enku.json"
FILE_FULLPATH = str(app_data_path) + "\\" + JSON_FILENAME

print(FILE_FULLPATH)

def save_password_to_file(data:dict):

    app_data = read_data()
    app_data["passwords"].append(data)

    write_data(app_data)


def write_data(app_data:dict) -> None:

    with open(FILE_FULLPATH, "w") as json_file:
        json.dump(app_data, json_file)


def read_data() -> dict:

    with open(FILE_FULLPATH) as json_file:
        return json.loads(json_file.read())


if pathlib.Path(FILE_FULLPATH).exists():
    print("Enku vault file found !")
    app_data = read_data()
else:
    print("Enku vault not file found ! \n Creating initial data file")
    app_data = {
        "settings" : {
            "theme": "light"
        },
        "passwords" : []
    }
    write_data(app_data)
    print("Enku vault file created.")
