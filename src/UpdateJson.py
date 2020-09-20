import json

def UpdateJsonLanguage(languages):
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["languages"] = languages

    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def UpdateJsonName(name):
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    for p in data['personalInformation']:
        p["name"] = name

    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def UpdateJsonAge(age):
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    for p in data['personalInformation']:
        p["age"] = age

    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile)