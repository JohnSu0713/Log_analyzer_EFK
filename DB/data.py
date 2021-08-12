

class ProductData():  # SV300G3
    def __init__(self):
        self.product_types = ('C1040',
                              'C2010',
                              'C2030',
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
            ('PCIe Correctable error', 'fw', {"query": "query_PCIe"}),
            ('PCIe Uncorrectable error', 'fw', {
             "query": "query_PCIe Uncorrectable"}),
            ('temperature error', 'temperature',
             {"query": "query_temperature"}),
            ('voltage error', 'Voltage', {"query": "query_Voltage"}),
            ('QPI Error', 'cpu', {"query": "query_QPI"}),
            ('ierr', 'cpu', {"query": "query_ierr"}),
            ('mcerr', 'cpu', {"query": "query_mcerr"}),
            ('Uncorrectable ECC', 'memory', {
             "query": "query_Uncorrectable ECC"}),
            ('correctable ECC', 'cpu', {"query": "query_correctable ECC"}),
            ('fan error', 'fan', {"query": "query_fan error"}),
            ('bmc Health error', 'management subsystem health',
             {"query": "query_bmc"}),
            ('psu error', 'psu', {"query": "query_psu"}),
            ('battery error', 'Battery', {"query": "query_battery"}),
        )
