import json

def CreateObjects(thing):
    for key in thing.__dict__:
        if(type(thing.__dict__[key]) == dict):
            newObj = jsonObj(thing.__dict__[key])
            thing.__dict__[key] = newObj
            CreateObjects(thing.__dict__[key])
        elif (type(thing.__dict__[key]) == list):
            for i in range(len(thing.__dict__[key])):
                newObj = jsonObj(thing.__dict__[key][i])
                thing.__dict__[key][i] = newObj
                CreateObjects(thing.__dict__[key][i])
                

class JsonReader:
    def __init__(self, file_loc_):
        self.file_loc =  file_loc_
        self.read_json()

    def read_json(self):
        #Reassign self.__dict__ to json map.
        jsonStrng = ""
        with open(self.file_loc, 'r') as fil:
            jsonStrng = fil.read()
        self.__dict__ = json.loads(jsonStrng)
        CreateObjects(self)


    def __getitem__(self, thing):
        return self.__dict__[thing]

class JsonStringReader:
    def __init__(self, strng):
        self.strng = strng 
        self.read_json()

    def read_json(self):
        #Reassign self.__dict__ to json map.
        jsonStrng = self.strng
        self.__dict__ = json.loads(jsonStrng)
        CreateObjects(self)


    def __getitem__(self, thing):
        return self.__dict__[thing]
class jsonObj:
    def __init__(self, thing):
        self.__dict__ = thing
        CreateObjects(self)