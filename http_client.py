import time
import requests
import threading
import os
import json
import re

from subprocess import run

from dotenv import load_dotenv
load_dotenv()


FLUENTD_IP = os.getenv("FLUENTD_IP")
FLUENTD_PORT = os.getenv("FLUENTD_PORT")
url = f"http://{FLUENTD_IP}:{FLUENTD_PORT}/sel.log"


payload = json.dumps([
    {
        "raw_message": "842 | 07/27/2021 | 13:18:24 | Voltage P3V_BAT | Lower Critical going low  | Deasserted | Reading 2.74 < Threshold 2.70 Volts"
    },
    {
        "raw_message": " 843 | 07/27/2021 | 14:30:17 | Voltage P3V_BAT | Lower Critical going low  | Asserted | Reading 2.70 < Threshold 2.70 Volts"
    },
    {
        "raw_message": " 843 | 07/27/2021 | 14:30:17 | Voltage P3V_BAT | Lower Critical going low  | Asserted | Reading 2.70 < Threshold 2.70 Volts"
    }
])
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# sel = run(['ipmitool', 'fru', 'print'], capture_output=True, text=True).stdout.splitlines()
# # log_list = json.dumps([{"raw_message": line} for line in sel])
# print(sel[2])

# raw_fru = run(['ipmitool', 'fru', 'print'],
#                 capture_output=True, text=True).stdout.splitlines()
# fru_info = []
# fru_regex = re.compile(r'\:([^:]+)')

# for line in raw_fru:
#     if "Product Name".lower() in line.lower():
#         fru_content = fru_regex.search(line)
#         fru_info.append(fru_content.group(1).strip())
#     if "Product Part Number".lower() in line.lower():
#         fru_content = fru_regex.search(line)
#         fru_info.append(fru_content.group(1).strip())
#     if "Product Serial".lower() in line.lower():
#         fru_content = fru_regex.search(line)
#         fru_info.append(fru_content.group(1).strip())


import threading
import time

# 子執行緒的工作函數
def job(k):
  for i in range(5):
    print(f"Child thread:{k}", i)
    time.sleep(1)


threads = []
for i in range(5):
    threads.append(threading.Thread(target = job, args=[i]))
    threads[i].start()


# # 建立一個子執行緒
# t = threading.Thread(target = job, args=[1])
# t2 = threading.Thread(target = job,  args=[2])
# t3 = threading.Thread(target = job,  args=[3])

# # 執行該子執行緒
# t.start()
# t2.start()
# t3.start()

# # 主執行緒繼續執行自己的工作
# for i in range(3):
#   print("Main thread:", i)
#   time.sleep(1)

# 等待 t 這個子執行緒結束
for thread in threads:
    thread.join()

print("Done.")
