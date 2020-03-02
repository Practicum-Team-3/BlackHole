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

        ### initialize Machine Settings window attributes
        self.baseMemory = 4
        self.bootOrder_floppy = False
        self.bootOrder_optical = False
        self.bootOrder_hardDisk = False
        self.bootOrder_network = False
        self.chipset = ''
        self.pointingDevice = ''
        self.extFeat_enableIO = False
        self.extFeat_enableEFI = False
        self.extFeat_hwClockUTCtime = False
        self.processors = 1
        self.exeCap = 100
        self.extFeat_enablePAE_NX = False
        self.paravirtInterface = ''
        self.hdVirt_enableVTx = False
        self.hdVirt_enableNestedPaging = False
        ### end machine settings window attributes

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

        ### machine settings window fields
        self.baseMemory = jsonObject['baseMemory']
        self.bootOrder_hardDisk = jsonObject['bootOrder_hardDisk']
        self.bootOrder_optical = jsonObject['bootOrder_optical']
        self.bootOrder_floppy = jsonObject['bootOrder_floppy']
        self.bootOrder_network = jsonObject['bootOrder_network']
        self.chipset = jsonObject['chipset']
        self.pointingDevice = jsonObject['pointingDevice']
        self.extFeat_enableIO = jsonObject['extFeat_enableIO']
        self.extFeat_enableEFI = jsonObject['extFeat_enableEFI']
        self.extFeat_hwClockUTCtime = jsonObject['extFeat_hwClockUTCtime']
        self.processors = jsonObject['processors']
        self.exeCap = jsonObject['exeCap']
        self.extFeat_enablePAE_NX = jsonObject['extFeat_EnablePAE_NX']
        self.paravirtInterface = jsonObject['paravirtInterface']
        self.hdVirt_enableVTx = jsonObject['hdVirt_enableVTx']
        self.hdVirt_enableNestedPaging = jsonObject['hdVirt_enableNestedPaging']
        self.shared_folders = BHSharedFolders(jsonObject['shared_folders'])
        self.network_settings = BHNetworkSettings(jsonObject['network_settings'])
        self.provisions = BHProvisions(jsonObject['provisions'])
        ### end machine settings window fields

    #returns a JSON string version of this object
    def toJSON(self):
        pass

    ### getter and setter for machine settings
    def getBaseMemory(self):
        return self.baseMemory

    def setBaseMemory(self, baseMemory):
        self.baseMemory = baseMemory

    def getBootOrder_hardDisk(self):
        return self.bootOrder_hardDisk

    def setBootOrder_hardDisk(self, bootOrder_hardDisk):
        self.bootOrder_hardDisk = bootOrder_hardDisk

    def getBootOrder_optical(self):
        return self.bootOrder_optical

    def setBootOrder_optical(self, bootOrder_optical):
        self.bootOrder_optical = bootOrder_optical

    def getBootOrder_floppy(self):
        return self.bootOrder_floppy

    def setBootOrder_floppy(self, bootOrder_floppy):
        self.bootOrder_floppy = bootOrder_floppy

    def getBootOrder_network(self):
        return self.bootOrder_network

    def setBootOrder_network(self, bootOrder_network):
        self.bootOrder_network = bootOrder_network

    def getChipset(self):
        return self.chipset

    def setChipset(self, chipset):
        self.chipset = chipset

    def getPointingDevice(self):
        return self.pointingDevice

    def setPointingDevice(self, pointingDevice):
        self.pointingDevice = pointingDevice

    def getExtFeat_enableIO(self):
        return self.extFeat_enableIO

    def setExtFeat_enableIO(self, extFeat_enableIO):
        self.extFeat_enableIO = extFeat_enableIO

    def getExtFeat_enableEFI_network(self):
        return self.extFeat_enableEFI

    def setExtFeat_enableEFI(self, extFeat_enableEFI):
        self.extFeat_enableEFI = extFeat_enableEFI

    def getExtFeat_hwClockUTCtime(self):
        return self.extFeat_hwClockUTCtime

    def setExtFeat_hwClockUTCtime(self, extFeat_hwClockUTCtime):
        self.extFeat_hwClockUTCtime = extFeat_hwClockUTCtime

    def getProcessors(self):
        return self.processors

    def setProcessors(self, processors):
        self.processors = processors

    def getExeCap(self):
        return self.exeCap

    def setExeCap(self, exeCap):
        self.exeCap = exeCap

    def getExtFeat_enablePAE_NX(self):
        return self.extFeat_enablePAE_NX

    def setExtFeat_enablePAE_NX(self, extFeat_enablePAE_NX):
        self.extFeat_enablePAE_NX = extFeat_enablePAE_NX
    
    def getParavirtInterface(self):
        return self.paravirtInterface

    def setParavirtInterface(self, paravirtInterface):
        self.paravirtInterface = paravirtInterface

    def getHdVirt_enableVTx(self):
        return self.hdVirt_enableVTx

    def setHdVirt_enableVTx(self, hdVirt_enableVTx):
        self.hdVirt_enableVTx = hdVirt_enableVTx

    def getHdVirt_enableNestedPaging(self):
        return self.hdVirt_enableNestedPaging

    def setHdVirt_enableNestedPaging(self, hdVirt_enableNestedPaging):
        self.hdVirt_enableNestedPaging = hdVirt_enableNestedPaging
    ### end getter and setter for machine settings

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





    