import pexpect
from .base import Controller


class MovistarHGUMitraStarController(Controller):

    def __init__(self, host, user, password):
        self.__host = host
        self.__user = user
        self.__password = password

    def _get_lan_hosts_mock(self):
        return """lanhosts show all
Bridge br0
Active   MAC Addr           IP Addr          ETH port  VLAN ID
 [v]     12:34:56:78:9a:bc  192.168.0.10     unknown   0        DHCP
 """

    def _get_lan_hosts(self):
        child = pexpect.spawn(f"ssh {self.__user}@{self.__host}")
        child.expect(f"{self.__user}@{self.__host}'s password: ")
        child.sendline(self.__password)
        child.expect(' fail to read file > ')
        child.sendline('lanhosts show all')
        child.expect('> ')
        cmd_show_data = child.before
        cmd_show_data_decoded = cmd_show_data.decode('utf-8')
        child.sendline("exit")

        return cmd_show_data_decoded

    @staticmethod
    def _get_connected_macs(content):
        macs = set()
        for line in content.split("\n"):
            if "[" in line:
                parsed_line = ' '.join(line.split()).split()
                if "v" in parsed_line[0]:
                    macs.add(parsed_line[1].lower())

        return macs

    def get_connected_devices(self, hosts):
        lanhost_output = self._get_lan_hosts()
        return [x for x in self._get_connected_macs(lanhost_output) if x in hosts]
