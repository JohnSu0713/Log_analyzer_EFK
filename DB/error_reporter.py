import json
from pprint import pprint
from beautifultable import BeautifulTable

# re_dict["responses"][query_index]['hits']['hits'][query_results_index]
# r_d["responses"][query_index]['hits']["total"]["value"]

# query_list = [{query: query_01}, {query: query_02}, {query: query_03}...]


class ErrorReporter():
    def __init__(self, response, pattern_list):
        self.pattern_list = pattern_list
        self.response = json.loads(response.text)
        self.error_list = []

    def error_recorder(self):
        for query_index in range(len(self.pattern_list)):
            # if exist specific pattern: append to error_list.
            if self.response["responses"][query_index]['hits']["total"]["value"] != 0:

                self.error_list.append(
                    (self.pattern_list[query_index],
                     self.response["responses"][query_index]['hits']["total"]["value"]))

    def show_error(self):
        print("########## found Error Pattern ##########")
        error_table = BeautifulTable()
        # error_table.rows.append(["Id", "Error", "Sensor", "Frequency"])
        error_table.rows.append(["Id", "Error", "Sensor", "Frequency"])

        for error, frequency in self.error_list:
            error_table.rows.append(
                [error.id, error.error, error.sensor, frequency])
        print(error_table)

############## Use Case #################
# sender = QuerySender(pattern_list)    #
# sender.multi_error_query()            #
# response = sender.send_query()        #
# ErrorReporter(response, pattern_list) #
#########################################
