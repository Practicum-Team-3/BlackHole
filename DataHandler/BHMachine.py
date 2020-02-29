class BHMachine(object):
    def __init__(self, name, os):
        self.name = name
        self.os = os
        self.sharedFolders = []
        self.IPAddresses = []
        self.network_type = ''
        self.network_name = ''
        self.auto_config = ''

    
class IPAddress(object):
    def __init__(self):
        pass

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
}