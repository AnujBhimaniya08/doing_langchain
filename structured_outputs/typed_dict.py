from typing import TypedDict

class person(TypedDict):
    name : str
    age : int

new_dict : person = {'name' : "sura", 'age' : 34}
print(new_dict)