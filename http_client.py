import requests
import json
import os
import time


def logs_from_file(path):
    '''
    Debug usage.
    '''
    with open(path) as f:
        return f.read()


def post_log(url, logs, tag):
    '''
    Post logs to specific url and tag.
    Tag = SN.PN.Model_name.Log_type
    '''
    url = url + f"/{tag}"
    print(url)
    log_list = [{"raw_message": line} for line in logs.splitlines()]
    json_list = json.dumps(log_list)
    # Send multiple events as a JSON array
    os.system(f"curl -X POST -d 'json={json_list}' {url}")


if __name__ == "__main__":
    # logs = logs_from_file('/Users/johnsu/Desktop/wiwynn_/logs/SEL_6.log')
    # url = "http://localhost:9880"
    # tag = "sel.log"
    post_log(url, logs, tag)
