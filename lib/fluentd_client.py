import os
import re
import json
import requests
import lib.ipmi
import lib.system

from subprocess import run
from dotenv import load_dotenv
load_dotenv()


class FluentdClient():

    def __init__(self):
        # Get Fluentd ip/port info from the env
        self.ip = os.getenv("FLUENTD_IP")
        self.port = None
        # Send logs to Fluentd
        # url = f"http://{self.ip}:{self.port}/{log_type}"
        self.log_list = None
        self.fru_info = None

    def get_fru(self):
        # ipmitool fru print cmd
        raw_fru = run(['ipmitool', 'fru', 'print'],
                      capture_output=True, text=True).stdout.splitlines()

        fru_info = []
        fru_regex = re.compile(r'\:([^:]+)')

        for line in raw_fru:
            if "Product Name".lower() in line.lower():
                fru_content = fru_regex.search(line)
                fru_info.append(fru_content.group(1).strip())
            if "Product Part Number".lower() in line.lower():
                fru_content = fru_regex.search(line)
                fru_info.append(fru_content.group(1).strip())
            if "Product Serial".lower() in line.lower():
                fru_content = fru_regex.search(line)
                fru_info.append(fru_content.group(1).strip())

        self.fru_info = fru_info

    def merge_fru(self):
        for message in self.log_list:
            for info in self.fru_info:
                message["raw_message"] = f"{info} | " + message["raw_message"]

    def send_logs(self, log_type):
        # Dump SEL or dmesg by log type define:
        if log_type.lower() == "sel":
            sel = lib.ipmi.Ipmi()
            sel.dump_sels()
            self.log_list = sel.log_list
            self.port = os.getenv("SEL_PORT")

        elif log_type.lower() == "dmesg":
            syslog = lib.system.System()
            syslog.dump_dmesg()
            self.log_list = syslog.log_list
            self.port = os.getenv("DMESG_PORT")

        self.get_fru()
        self.merge_fru()
        url = f"http://{self.ip}:{self.port}/{log_type.lower()}.log"

        # Send logs to Fluentd
        payload = json.dumps(self.log_list)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request(
            "POST", url, headers=headers, data=payload)
        print(response)


# Debug
# if __name__ == "__main__":
#     my_fluentd_client = FluentdClient()
#     my_fluentd_client.send_logs("dmesg")