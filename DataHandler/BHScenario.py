
class BHScenario(object):
    def __init__(self):
        self.machines = {"key":"machine"}
    
    def addMachine(self, machine):
        pass

    def setName(self):
        pass

    def setExploitInfo(self, exploitInfo):
        pass


class BHExploitInfo(object):
    def __init__(self):
        pass


class BHVulnerabilityInfo(object):
    def __init__(self):
        pass    


class BHNetworkSettings(object):
    def __init__(self):
        pass



    sample_scenario = '''{
    "scenario_name" : "name", 
    "id" : 123456789, 
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
        "name": "attacker",
        "shared_folders": [
            "./attackerfiles",
            "/sharedfolder"
        ],
        "network_settings": {
            "ip_address": "192.168.50.5",
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        },
        "provisions": [
            {
            "name": "installE0",
            "commands": [
            [
                "shell",
                "./../../sharedfolder/e0.sh"
            ]
            ]
        }]
        },
        {
        "os": "debian",
        "name": "victim",
        "shared_folders": [
            "./attackerfiles",
            "/sharedfolder"
        ],
        "network_settings": {
            "ip_address": "192.168.50.5",
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        },
        "provisions": [
            {
            "name": "installE0",
            "commands": [
            [
                "shell",
                "./../../sharedfolder/e0.sh"
            ]
            ]
        }]
        }
    ],
    "network_settings" : {
            "network_type" : "type", 
            "network_name" : "Name", 
            "auto_config" : "True"
        }
    }'''