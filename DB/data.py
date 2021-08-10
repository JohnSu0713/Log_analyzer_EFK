

class ProductData():  # SV300G3
    def __init__(self):
        self.product_types = ('SV300G3',
                              'SV200G4',
                              'SV500Z4',
                              'SK300R5',
                              'SV620G9')


class SensorData():  # CPU, FAN ...
    def __init__(self):
        self.sensor_types = ('fw',
                             'bus',
                             'temperature',
                             'Voltage',
                             'cpu',
                             'memory',
                             'pcie',
                             'fan',
                             'management subsystem health',
                             'psu',
                             'Battery')


class ErrorData():
    def __init__(self):
        self.error_types = (
            ('PCIe Correctable error', 'fw', 'all'),
            ('PCIE Uncorrectable error', 'fw', 'all'),
            ('temperature error', 'temperature', 'all'),
            ('voltage error', 'Voltage', 'all'),
            ('QPI Error', 'cpu', 'all'),
            ('ierr', 'cpu', 'all'),
            ('mcerr', 'cpu', 'all'),
            ('Uncorrectable ECC', 'memory', 'all'),
            ('correctable ECC', 'cpu', 'all'),
            ('fan error', 'fan', 'all'),
            ('bmc Health error', 'management subsystem health', 'all'),
            ('psu error', 'psu', 'all'),
            ('battery error', 'Battery', 'all'),
        )
