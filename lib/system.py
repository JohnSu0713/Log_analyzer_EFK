from subprocess import run


class System():
    def __init__(self):
        self.dmesg_list = None

    def dump_dmesg(self):
        # Execute the 'dmesg' cmd by popen lib
        self.dmesg_list = run(['dmesg'],
                              capture_output=True, text=True).stdout.splitlines()
