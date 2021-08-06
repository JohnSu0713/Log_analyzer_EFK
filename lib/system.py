from subprocess import run


class System():
    def __init__(self):
        self.raw_logs = None
        self.log_list = None

    def dump_dmesg(self):
        # Dmesg command handeler
        self.raw_logs = run(['dmesg'],
                            capture_output=True, text=True).stdout

        self.log_list = [{"raw_message": line}
                         for line in self.raw_logs.splitlines()]
