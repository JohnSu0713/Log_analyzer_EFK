

class ProductData():  # SV300G3
    def __init__(self):
        self.product_types = ('C1040',
                              'C2010',
                              'C2030',
                              'ambrose'
                              )


class ProjectData():  # SV300G3
    def __init__(self):
        self.project_types = ('F',
                              'T',
                              'A',
                              'N',
                              'S')


# class SensorData():  # CPU, FAN ...
#     def __init__(self):
#         self.sensor_types = ('fw',
#                              'bus',
#                              'temperature',
#                              'Voltage',
#                              'cpu',
#                              'memory',
#                              'pcie',
#                              'fan',
#                              'management subsystem health',
#                              'psu',
#                              'Battery')


# class ErrorData():
#     def __init__(self):
#         self.error_types = ('PCIe Correctable error',
#                             'PCIE Uncorrectable error',
#                             'temperature error',
#                             'voltage error',
#                             'QPI Error',
#                             'ierr',
#                             'mcerr',
#                             'Uncorrectable ECC',
#                             'correctable ECC',
#                             'fan error',
#                             'bmc Health error', 'management subsystem health',
#                             'psu error',
#                             'battery error',
#                             )

# class Product_Data():
#     def __init__(self):
#         self.prodct_data = (
#             ('SV300G3', 'PCIe Correctable error')
#             ('SV300G3', 'temperature error')
#             ('SV300G3', 'voltage error')
#             ('SV300G3', 'Uncorrectable ECC')
#             ('SV300G3', 'ierr')
#             ('SV104X3', 'correctable ECC')
#             ('SV104X3', 'psu error')
#             ('SV104X3', 'bmc Health error')
#             ('SV104X3', 'battery error')
#             ('SV304X3', 'voltage error')
#             ('SV304X3', 'fan error')
#             ('DF330G3', 'PCIe Uncorrectable error')
#             ('SV45003', 'PCIe Uncorrectable error')
#         )


class ErrorData():
    def __init__(self):
        self.error_data = (
            ('PCIe Correctable error', 'fw', {"track_total_hits":True,"min_score":5,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"message":{"query":"correctable","boost":5}}}],"should":{"match":{"message":{"query":"bus","boost":10}}}}},"size":100}),
            ('PCIe Uncorrectable error', 'fw', {"track_total_hits":True,"min_score":5,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"message":{"query":"uncorrectable","boost":5}}}],"should":{"match":{"message":{"query":"bus","boost":10}}}}},"size":100}),
            ('temperature error', 'temperature',{"track_total_hits":True,"min_score":1,"query":{"bool":{"must":{"match":{"status":"asserted"}},"should":{"match":{"sensor":{"query":"temperature","boost":10}}}}},"size":100}),
            ('voltage error', 'Voltage', {"track_total_hits":True,"min_score":1,"query":{"bool":{"must":{"match":{"status":"asserted"}},"should":{"match":{"sensor":{"query":"voltage","boost":10}}}}},"size":100}),
            ('QPI Error', 'cpu', {"track_total_hits":True,"min_score":10,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"sensor":{"query":"Processor"}}}],"should":[{"match":{"message.keyword":{"query":" ","boost":10}}},{"match":{"sensor":{"query":"QPI","boost":10}}}]}},"size":1000}),
            ('ierr', 'cpu', {"track_total_hits":True,"min_score":10,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"sensor":{"query":"Processor"}}}],"should":{"match":{"message":{"query":"IERR","boost":10}}}}},"size":1000}),
            ('mcerr/ other_CPU Error', 'cpu', {"track_total_hits":True,"min_score":10,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"sensor":{"query":"Processor"}}}],"should":{"match":{"message.keyword":{"query":" ","boost":10}}}}},"size":1000}),
            ('Uncorrectable ECC', 'memory', {"track_total_hits":True,"min_score":10,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"message":{"query":"uncorrectable","boost":5}}}],"should":{"match":{"sensor":{"query":"memory","boost":10}}}}},"size":100}),
            ('correctable ECC', 'memory', {"track_total_hits":True,"min_score":10,"query":{"bool":{"must":[{"match":{"status":"asserted"}},{"match":{"message":{"query":"correctable","boost":5}}}],"should":{"match":{"sensor":{"query":"memory","boost":10}}}}},"size":100}),
            ('fan error', 'fan', {"track_total_hits":True,"min_score":1,"query":{"bool":{"must":{"match":{"status":"asserted"}},"should":{"match":{"sensor":{"query":"fan","boost":10}}}}},"size":100}),
            ('bmc Health error', 'management subsystem health', {"track_total_hits":True,"min_score":1,"query":{"bool":{"must":{"match":{"status":"asserted"}},"should":{"match":{"sensor":{"query":"management","boost":10}}}}},"size":100}),
            ('psu error', 'psu', {"track_total_hits":True,"min_score":1,"query":{"bool":{"must":{"match":{"status":"asserted"}},"should":{"match":{"sensor":{"query":"Power supply","boost":10}}}}},"size":100}),
            ('battery error', 'Battery', {"track_total_hits":True,"min_score":1,"query":{"bool":{"must":{"match":{"status":"asserted"}},"should":{"match":{"sensor":{"query":"battery","boost":10}}}}},"size":100}),
            ('kernal panic error', 'multi_ref', {"track_total_hits":True,"min_score": 10,"query":{"bool":{"should":[{"match":{"dmesg_mesg":{"query":"panic","boost":10}}},{"match":{"sensor":{"query":"kernel","boost":10}}}]}},"size":100}),
            ('covid-19 error', 'multi_ref', {"track_total_hits":True,"min_score": 10,"query":{"bool":{"filter":[{"bool":{"should":[{"match":{"sensor":{"query":"virous","boost":10}}},{"match":{"dmesg_mesg":{"query":"covid","boost":10}}},{"match":{"sel_mesg":{"query":"corona","boost":10}}}]}}]}},"size":100}),
        )
