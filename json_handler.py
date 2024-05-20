import json

def json_reader() -> list[dict]:
    """
    Me permite leer un archivo json y devolver su informacion en formato list[dict]
    """
    data = []
    with open('data.json',"r") as json_reader:
        data = json.load(json_reader)
    return data

def json_writer(data) -> None:
    """
    Me permite escribir en un archivo json información
    """
    with open('data.json','w') as json_writer:
        json.dump(data, json_writer)