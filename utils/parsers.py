import json
from dataclasses import dataclass

@dataclass
class Config:
    token: str
    admins: list

def config(path="./config.json") -> Config:
    try:
        with open(path) as file:
            result = json.load(file)
        return result
    except FileExistsError:
        return "Does config file exist? Check your path"
    except json.JSONDecodeError:
        return "JSON Decode error. Check your config file"