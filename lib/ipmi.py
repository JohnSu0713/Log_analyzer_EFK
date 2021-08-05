from subprocess import run
import re


class Ipmi():
    def __init__(self):
        self.raw_logs = None
        self.sel_list = None
        self.fru_info = None

    def send_cmd(self):
        # IPMI command handeler
        self.raw_logs = run(['ipmitool', 'sel', 'elist'],
                            capture_output=True, text=True).stdout

    def list_sels(self):
        # ipmitool sel elist
        self.sel_list = [{"raw_message": line}
                         for line in self.raw_logs.splitlines()]

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
        for message in self.sel_list:
            for info in self.fru_info:
                message["raw_message"] = f"{info} | " + message["raw_message"]
        
# {'raw_message': 'B81019Z1000572800008J0SA | B81.019Z1.0005 | SV300G3 |    4 | 06/05/2021 | 15:40:25 | Temperature Inlet Temp1 | Upper Critical going high | Asserted | Reading 40 > Threshold 40 degrees C'}
# {'raw_message': <Product Serial>  | < Product Part Number> | <Product Name> |    4 | 06/05/2021 | 15:40:25 | Temperature Inlet Temp1 | Upper Critical going high | Asserted | Reading 40 > Threshold 40 degrees C'}