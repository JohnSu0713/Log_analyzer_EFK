import os
import json
import requests

from lib import ipmi, system
from dotenv import load_dotenv
load_dotenv()


class FluentdClient():

    def __init__(self):
        # TODO: Get Fluentd ip/port info from the env
        self.ip = os.getenv("FLUENTD_IP")
        self.port = os.getenv("FLUENTD_PORT")
        # Send logs to Fluentd
        # url = f"http://{self.ip}:{self.port}/{log_type}"
        self.url = f"http://{self.ip}:{self.port}/sel.log"
        self.log_list = None

    def send_logs(self, log_type):
        # Dump SEL or dmesg by log type define:
        if log_type.lower() == "sel":
            sel = ipmi.Ipmi()
            sel.send_cmd()
            sel.list_sels()
            sel.get_fru()
            sel.merge_fru()
            self.log_list = sel.sel_list

        elif log_type.lower() == "dmesg":
            syslog = system.System()
            syslog.dump_dmesg()
            self.log_list = syslog.dmesg_list

        # Send logs to Fluentd
        payload = json.dumps(self.log_list)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request(
            "POST", self.url, headers=headers, data=payload)


# Debug
# if __name__ == "__main__":
#     my_fluentd_client = FluentdClient()
#     my_fluentd_client.send_logs("SEL")
