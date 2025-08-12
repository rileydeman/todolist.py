from config.variables import *
from pathlib import Path
import os
import json


# Variables
DIR_PATH = Path(DIR_PATH)
dataFileDir = DIR_PATH / 'list-data.json'

def checkDataFile():

    if os.path.exists(dataFileDir):
        print("lists-data.json File Exists")
    else:
        print("lists-data.json File Not Exists")
        createDataFile()


def createDataFile():
    dataFileDir.parent.mkdir(parents=True, exist_ok=True)

    standardData = {
        "credits": {
            "todoApp": {
                "name": "GhostList",
                "createdWith": "Python",
                "copyright": "(c) rileydeman",
                "license": "personal and educational use only"
            },
            "developer": {
                "name": "Riley de Man",
                "website": "https://www.rileydeman.com"
            }
        },
        "lists": []
    }

    with open(dataFileDir, "w") as f:
        json.dump(standardData, f, indent=4)