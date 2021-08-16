import requests
import json


class QuerySender():
    def __init__(self, pattern_list) -> None:
        self.query_list = [pattern.query for pattern in pattern_list]
        self.sensor_list = [pattern.sensor for pattern in pattern_list]
        self.error_list = [pattern.error for pattern in pattern_list]
        self.project_list = [pattern.project for pattern in pattern_list]
        self.payload = None
        self.url = "http://172.17.254.187:9200/_msearch"

    def conditional_filter(self, SN=None, PN=None, PPN=None):
        '''
        Input the condition(s) and add the condition filter to each query.
        '''
        if SN:
            for query in self.query_list:
                query['query']['bool']['filter'] = [{"match": {"SN": SN}}]
        elif PN:
            for query in self.query_list:
                query['query']['bool']['filter'] = [
                    {"match": {"project_name": PN}}]
        elif PPN:
            for query in self.query_list:
                query['query']['bool']['filter'] = [{"match": {"PPN": PPN}}]

    def multi_error_query(self):
        '''
        Input: A list of query request ready to send.
        output: /_msearch required string schema.
        '''
        payload = '''{ }\n'''
        for query in self.query_list:
            payload += json.dumps(query)
            payload += '\n{ }\n'
        self.payload = payload

    def send_query(self):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request(
            "GET", self.url, headers=headers, data=self.payload)
        return response


############## Use Case ##############
# sender = QuerySender()             #
# sender.multi_error_query()         #
# response = sender.send_query()     #
######################################
