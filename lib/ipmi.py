from subprocess import run


class Ipmi():
    def __init__(self):
        self.raw_logs = None
        self.log_list = None

    def dump_sels(self):
        '''
        '{"raw_message": "B81019Z1000572800008J0SA | B81.019Z1.0005 | SV300G3 | 1bf | 06/10/2021 | 02:36:04 | Voltage P3V_BAT | Lower Critical going low  | Asserted | Reading 2.70 < Threshold 2.70 Volts"}'
        {SN} | {PPN} | {Product_name} | {index} | {date} | {time} | {sensor} | message  | {status} | ( {error} )
        '''
        # Dmesg command handeler
        self.raw_logs = run(['ipmitool', 'sel', 'elist'],
                            capture_output=True, text=True).stdout

        self.log_list = [{"raw_message": line}
                         for line in self.raw_logs.splitlines()]

