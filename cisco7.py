import netmiko
import pandas as pd
from getpass import getpass
import sys
import argparse


class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or 
    issue configuration commands
    """

    def __init__(self, ip, port=22, prompt=False, username=None, 
                        password=None, device_type='cisco_ios'):
        """
        Establishes connection to target device.
        
        :param str ip:              ip address of target device.
        :param int port:            port for connection
        :param str username:        username for authentication
        :param str password:        password for authentication
        :param str device_type:     should not change, class is designed for Cisco IOS
        """
        if prompt:
            username = input('Username: ')
            password = getpass()
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                        password=password, device_type=device_type)
        _ = self.conn.send_command('sh run | include hostname')
        self.hostname = _.split()[-1]

    def get_interface_list(self):
        """
        Returns list containing interface names from show ip interface brief
        """
        ip_int_br = self.conn.send_command('sh ip int br', use_textfsm=True)
        df = pd.DataFrame(ip_int_br)
        interface_names = df['intf'].to_list()
        return interface_names

    def get_run_int(self):
        """
        Returns output from sh run | section [interface-name] command
        Type case-sensitive interface name when prompted
        """
        section = input('Interface: ')
        if section in self.get_interface_list():
            return self.conn.send_command('sh run | section ' + section)
        else:
            return 'Error - Invalid interface name.'

class CiscoIOS_CLI(CiscoIOS):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'ip', 
            type=str, 
            help='IP address, SSH endpoint'
        )
        parser.add_argument(
            '--port', 
            type=int, 
            default=22, 
            help='Port for connection'
        )
        parser.add_argument(
            '-u', '--username', 
            type=str, 
            help='Username for SSH connection'
        )
        parser.add_argument(
            '-p', '--password', 
            type=str, 
            help='Password for SSH connection'
        )
        parser.add_argument(
            '--device_type', 
            type=str, 
            default='cisco_ios', 
            help='Device type of appliance'
        )
        
        args = parser.parse_args()

        ip = args.ip
        port = args.port
        username = args.username
        password = args.password
        device_type = args.device_type
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
            password=password, device_type=device_type)
        print(self.conn.send_command('show run | include hostname'))

    def get_interface_list(self):
        return super().get_interface_list()

    def get_run_int(self):
        return super().get_run_int()

def main():
   # csr = CiscoIOS(sys.argv[1], username='cisco', password='cisco')
   csr = CiscoIOS_CLI()
   print(csr.get_interface_list())

if __name__ == '__main__':
    main()