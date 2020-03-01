import json

class BHMachine(object):
    def __init__(self, machineJSON=''):
        self.name = ''
        self.id = -1
        self.os = ''
        self.type = ''
        self.shared_folders = None #should be list
        self.network_settings = None #should be dictionary
        self.provisions = None #should be list

        if machineJSON != '':
            self.fromJSON(machineJSON)

    #returns a dictionary containing some of the important information fields of this machine
    def getFieldsToShow(self):
        fields = {"name": str(self.name), "os": str(self.os)}
        return fields

    def getOS(self):
        return str(self.os)

    def isVictim(self):
        return self.type == 'victim'

    #gets the id of this machine
    def getMachineID(self):
        return self.id

    #sets the id of this machine
    def setMachineID(self, id):
        self.machineID = id

    #populates fields of this object from a JSON string
    def fromJSON(self, jsonObject):
        self.name = jsonObject['name']
        self.id = jsonObject['id']
        self.os = jsonObject['os']
        self.type = jsonObject['type']
        self.shared_folders = BHSharedFolders(jsonObject['shared_folders'])
        self.network_settings = BHNetworkSettings(jsonObject['network_settings'])
        self.provisions = BHProvisions(jsonObject['provisions'])

    #returns a JSON string version of this object
    def toJSON(self):
        pass


#HELPER CLASSES
class BHSharedFolders(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def getDict(self):
        return self.dictionary


class BHNetworkSettings(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def getDict(self):
        return self.dictionary


class BHProvisions(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def getDict(self):
        return self.dictionary