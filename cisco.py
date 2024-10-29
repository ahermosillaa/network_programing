import netmiko
import os


class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or 
    issue configuration commands
    """

    def __init__(self, ip, port=22, username=None, 
            password=None, device_type='cisco_ios'):
        """
        Establishes connection to target device.
        
        :param str ip:              ip address of target device.
        :param int port:            port for connection
        :param str username:        username for authentication
        :param str password:        password for authentication
        :param str device_type:     should not change, class is designed for Cisco IOS
        """
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                        password=password, device_type=device_type)
        _ = self.conn.send_command('sh run | include hostname')
        self.hostname = _.split()[-1]

    def get_IOS_version(self, key=''):
        """
        Returns IOS version as a string
        """
        self.version_data = self.conn.send_command('sh version', use_textfsm=True)
        if key:
            return self.version_data[key]
        else:
            return self.version_data[0]    