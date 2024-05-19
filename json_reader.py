import json

def json_reader() -> list[dict]:
    data = []
    with open('data.json',"r") as json_reader:
        data = json.load(json_reader)
    return data

def json_writer(data):
    with open('data.json','w') as json_writer:
        json.dump(data, json_writer)