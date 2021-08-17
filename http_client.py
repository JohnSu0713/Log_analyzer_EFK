# import time
# import requests
# import threading
# import os
# import json
# import re

# from subprocess import run

# from dotenv import load_dotenv
# load_dotenv()


# FLUENTD_IP = os.getenv("FLUENTD_IP")
# FLUENTD_PORT = os.getenv("FLUENTD_PORT")
# url = f"http://{FLUENTD_IP}:{FLUENTD_PORT}/sel.log"


# payload = json.dumps([
#     {
#         "raw_message": "842 | 07/27/2021 | 13:18:24 | Voltage P3V_BAT | Lower Critical going low  | Deasserted | Reading 2.74 < Threshold 2.70 Volts"
#     },
#     {
#         "raw_message": " 843 | 07/27/2021 | 14:30:17 | Voltage P3V_BAT | Lower Critical going low  | Asserted | Reading 2.70 < Threshold 2.70 Volts"
#     },
#     {
#         "raw_message": " 843 | 07/27/2021 | 14:30:17 | Voltage P3V_BAT | Lower Critical going low  | Asserted | Reading 2.70 < Threshold 2.70 Volts"
#     }
# ])
# headers = {
#     'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# # print(response.text)

# # sel = run(['ipmitool', 'fru', 'print'], capture_output=True, text=True).stdout.splitlines()
# # # log_list = json.dumps([{"raw_message": line} for line in sel])
# # print(sel[2])

# # raw_fru = run(['ipmitool', 'fru', 'print'],
# #                 capture_output=True, text=True).stdout.splitlines()
# # fru_info = []
# # fru_regex = re.compile(r'\:([^:]+)')

# # for line in raw_fru:
# #     if "Product Name".lower() in line.lower():
# #         fru_content = fru_regex.search(line)
# #         fru_info.append(fru_content.group(1).strip())
# #     if "Product Part Number".lower() in line.lower():
# #         fru_content = fru_regex.search(line)
# #         fru_info.append(fru_content.group(1).strip())
# #     if "Product Serial".lower() in line.lower():
# #         fru_content = fru_regex.search(line)
# #         fru_info.append(fru_content.group(1).strip())


# import threading
# import time

# # 子執行緒的工作函數
# def job(k):
#   for i in range(5):
#     print(f"Child thread:{k}", i)
#     time.sleep(1)


# threads = []
# for i in range(5):
#     threads.append(threading.Thread(target = job, args=[i]))
#     threads[i].start()


# # # 建立一個子執行緒
# # t = threading.Thread(target = job, args=[1])
# # t2 = threading.Thread(target = job,  args=[2])
# # t3 = threading.Thread(target = job,  args=[3])

# # # 執行該子執行緒
# # t.start()
# # t2.start()
# # t3.start()

# # # 主執行緒繼續執行自己的工作
# # for i in range(3):
# #   print("Main thread:", i)
# #   time.sleep(1)

# # 等待 t 這個子執行緒結束
# for thread in threads:
#     thread.join()

# print("Done.")


# import requests
# import json
# from pprint import pprint

# url = "http://172.17.254.187:9200/_msearch"

# payload = '''{ }\n'''

# q_list = [{"query": {"match": {"sensor": "kernel"}}},
#           {"query": {"match":

#                      {"sensor": "temperature"}}}]


# def conditional_filter(query_list, SN=None, PN=None, PPN=None):
#     if SN:
#         for query in query_list:
#             query['query']['bool']['filter'] = [{"match": {"SN": SN}}]
#     elif PN:
#         for query in query_list:
#             query['query']['bool']['filter'] = [
#                 {"match": {"project_name": PN}}]
#     elif PPN:
#         for query in query_list:
#             query['query']['bool']['filter'] = [{"match": {"PPN": PPN}}]


# def multi_error_query(query_list) -> str:
#     '''
#     Input: A list of query request ready to send.
#     output: /_msearch required string schema.
#     '''
#     payload = '''{ }\n'''
#     for query in query_list:
#         payload += json.dumps(query)
#         payload += '\n{ }\n'
#     return payload


# payload = multi_error_query(q_list)

# # payload = '''
# # { }
# # {"query":{"match":{"sensor":"kernel"}}}
# # { }
# # {"query":{"match":{"sensor":"temperature"}}}
# # '''
# headers = {
#     'Content-Type': 'application/json'
# }

# sent_dict = []

# q_dict = {"track_total_hits": True, "min_score": 5, "query": {"bool": {"must": [{"match": {"status": "asserted"}}, {"match": {
#     "message": {"query": "correctable", "boost": 5}}}], "should": {"match": {"message": {"query": "bus", "boost": 10}}}}}, "size": 100}
# q_dict['query']['bool']['filter'] = [{"match": {"sensor": "Memory"}},
#                                      {"match": {"SN": "B81019Z1000572800008J0SA"}}]
# # re_dict = json.loads(response.text)
# # pprint(re_dict["responses"][1]['hits']['hits'][3])

# test_Q = [{"track_total_hits": True, "query": {"bool": {"should": [{"match": {"dmesg_mesg": {
#     "query": "panic", "boost": 10}}}, {"match": {"sensor": {"query": "kernel", "boost": 10}}}]}}, "size": 20}]
# conditional_filter(test_Q, SN='B81019Z1000572800008J0SA')
# test_q = multi_error_query(test_Q)

# # pprint(test_Q)
# # print(len(re_dict["responses"]))

# response = requests.request("GET", url, headers=headers, data=test_q)
# r_d = json.loads(response.text)
# pprint(r_d["responses"][0]['hits']["total"]["value"])

# # re_dict["responses"][query_index]['hits']['hits'][query_results_index]


# ===================================================================
