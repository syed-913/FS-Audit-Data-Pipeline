#!/bin/python3
import os
import json

def os_flavor():
    try:
        json_file = "my_commands.json"
        with open(json_file,"r") as jf:
                commands_kv = json.load(jf)
                os_flavor = os.popen(commands_kv["os_flavor"]).read().strip('\n').lower()
                return os_flavor
    except Exception as e:
        return None 

def csv_file_creation():
    try:
        json_file = "my_commands.json"
        with open(json_file,"r") as jf:
            commands_kv = json.load(jf)
        os_flavor = os.popen(commands_kv["os_flavor"]).read().strip('\n').lower()
        cmd_for_csv = os.popen(commands_kv["df_cmd"]).read()
        if os_flavor not in ["aix", "solaris"]:
            return f"'FS_report.csv' has been updated! {cmd_for_csv}"
        else:
            return "New OS found", os_flavor 
    except Exception as e:
        return f"Something went wrong with the current distro", e
