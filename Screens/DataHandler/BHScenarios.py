from Screens.DataHandler.BHScenario import BHScenario
import json

class BHScenarios(object):
    def __init__(self):
        self.scenarios = {"key":"scenario"}

        self.testScenario = '''{
    "scenario_name" : "name", 
    "id" : 123, 
    "creation_date" : "string", 
    "last_accessed" : "string", 
    "exploit_info": {
            "name": "Name", 
            "download_link": "link", 
            "type": "type"
        }, 
    "vulnerability_info": {
            "name": "Name", 
            "cve_link": "url", 
            "download_link": "link", 
            "type": "type"
        }, 
    "machines": [
            {
            "os": "windows",
            "name": "attacker1",
            "id": 122,
            "type": "pov",
            "shared_folders": [],
            "network_settings": [],
            "provisions": [],
            "baseMemory": 5,
            "bootOrder_floppy": "False",
            "bootOrder_optical": "False",
            "bootOrder_hardDisk": "False",
            "bootOrder_network": "False",
            "chipset": "PIIX3",
            "pointingDevice": "PS/2 Mouse",
            "extFeat_enableIO": "False",
            "extFeat_enableEFI": "False",
            "extFeat_hwClockUTCtime": "False",
            "processors": 3,
            "exeCap": 99,
            "extFeat_EnablePAE_NX": "False",
            "paravirtInterface": "Default",
            "hdVirt_enableVTx": "False",
            "hdVirt_enableNestedPaging": "False"
        },
{
            "os": "windows",
            "name": "victim1",
            "id": 123,
            "type": "victim",
            "shared_folders": [],
            "network_settings": [],
            "provisions": [],
            "baseMemory": 5,
            "bootOrder_floppy": "False",
            "bootOrder_optical": "False",
            "bootOrder_hardDisk": "False",
            "bootOrder_network": "False",
            "chipset": "PIIX3",
            "pointingDevice": "PS/2 Mouse",
            "extFeat_enableIO": "False",
            "extFeat_enableEFI": "False",
            "extFeat_hwClockUTCtime": "False",
            "processors": 3,
            "exeCap": 99,
            "extFeat_EnablePAE_NX": "False",
            "paravirtInterface": "Default",
            "hdVirt_enableVTx": "False",
            "hdVirt_enableNestedPaging": "False"
        },
{
            "os": "windows",
            "name": "victim2",
            "id": 124,
            "type": "victim",
            "shared_folders": [],
            "network_settings": [],
            "provisions": [],
            "baseMemory": 5,
            "bootOrder_floppy": "False",
            "bootOrder_optical": "False",
            "bootOrder_hardDisk": "False",
            "bootOrder_network": "False",
            "chipset": "PIIX3",
            "pointingDevice": "PS/2 Mouse",
            "extFeat_enableIO": "False",
            "extFeat_enableEFI": "False",
            "extFeat_hwClockUTCtime": "False",
            "processors": 3,
            "exeCap": 99,
            "extFeat_EnablePAE_NX": "False",
            "paravirtInterface": "Default",
            "hdVirt_enableVTx": "False",
            "hdVirt_enableNestedPaging": "False"
        },
{
            "os": "windows",
            "name": "victim3",
            "id": 125,
            "type": "victim",
            "shared_folders": [],
            "network_settings": [],
            "provisions": [],
            "baseMemory": 5,
            "bootOrder_floppy": "False",
            "bootOrder_optical": "False",
            "bootOrder_hardDisk": "False",
            "bootOrder_network": "False",
            "chipset": "PIIX3",
            "pointingDevice": "PS/2 Mouse",
            "extFeat_enableIO": "False",
            "extFeat_enableEFI": "False",
            "extFeat_hwClockUTCtime": "False",
            "processors": 3,
            "exeCap": 99,
            "extFeat_EnablePAE_NX": "False",
            "paravirtInterface": "Default",
            "hdVirt_enableVTx": "False",
            "hdVirt_enableNestedPaging": "False"
        }
    ],
    "network_settings" : {
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        }
    }'''
        self.miniScenario = '''{
    "scenario_name" : "name", 
    "id" : 123, 
    "creation_date" : "string", 
    "last_accessed" : "string", 
    "exploit_info": {
            "name": "Name", 
            "download_link": "link", 
            "type": "type"
        }, 
    "vulnerability_info": {
            "name": "Name", 
            "cve_link": "url", 
            "download_link": "link", 
            "type": "type"
        }, 
    "machines": [],
    "network_settings" : {
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        }
    }'''

    
    def addScenario(self, scenario):
        pass

    def getScenario(self):
        testScenarioObject = BHScenario()
        scenarioJSONObject = json.loads(self.testScenario)
        testScenarioObject.fromJSON(scenarioJSONObject)
        return testScenarioObject
