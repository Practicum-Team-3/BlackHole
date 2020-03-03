# This Python file uses the following encoding: utf-8

# if__name__ == "__main__":
#     pass
NEWSCENARIO = '''
{
    "scenario_name": "new scenario",
    "scenario_id": "404",
    "creation_date": "02/03/2020 21:22:38",
    "last_accessed": "02/03/2020 21:22:38",
    "exploit_info": {
        "name": "test_name",
        "type": "test_type",
        "download_link": "test_download_link"
    },
    "vulnerability_info": {
        "name": "test_name",
        "type": "test_type",
        "cve_link": "test_cve_link",
        "download_link": "test_download_link"
    },
    "machines": {}
}'''

NEWMACHINE = '''
{
    "os": "windows",
    "name": "new machine",
    "is_attacker": false,
    "shared_folders": [
        "./attackerfiles",
        "/sharedfolder"
    ],
    "network_settings": {
        "network_name": "Network Name",
        "network_type": "Network Type",
        "ip_address": "192.168.50.5",
        "auto_config": true
    },
    "provisions": {
        "name": "pingVictim",
        "provision_type": "shell",
        "commands": [
            "pip install unique-id"
        ]
    },
    "gui": false
}
'''
