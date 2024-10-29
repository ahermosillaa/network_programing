"""
This module is designed to interact with Cisco appliances

"""
import netmiko
import pandas as pd
import requests
import pprint
import json

class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or
    issue configuration commands
    """

    def __init__(self, ip, port=22, username=None, password=None, device_type=None):
        """
        The constructor creates an instance variable connected to a cisco IOS router
        """
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                password=password, device_type=device_type)
        self.hostname = self.conn.send_command('sh run | include hostname').split()[-1]

    def get_interface_names(self):
        """
        Returns list containing interface names from show ip interface brief
        """
        ip_int_br = self.conn.send_command('sh ip int br', use_textfsm=True)
        df = pd.DataFrame(ip_int_br)
        interface_names = df['intf'].to_list()
        return interface_names

    def get_run_cfg(self):
        """
        Returns running configuration as string from the appliance
        """
        return self.conn.send_command('sh run')

class CiscoRestconf():
    """
    This class is designed to query and manage a Cisco appliance via restconf
    """
    def __init__(self, ip, username, password, port=443):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = str(port)

    def get_interface_info(self, data_type='json'):
        """
        Returns dictionary containing JSON interface information
        """
        url_base = 'https://' + self.ip + ':' + self.port
        dn = '/restconf/data/Cisco-IOS-XE-native:native/interface/'
        uri = url_base + dn
        headers = {'Accept':'application/yang-data+' + data_type}
        request_response = requests.get(uri,
            headers=headers, 
            auth=(self.username, self.password), 
            verify=False)
        return request_response.json()

    def get_interface_ips(self, interface_info, data_type='json'):
        """
        Returns list of interfaces that have a primary IP address
        """
        interface_dict = interface_info['Cisco-IOS-XE-native:interface']
        interface_list = interface_dict['GigabitEthernet']
        for intf in interface_list:
            if 'ip' not in intf: 
                interface_list.remove(intf)
        return json.dumps(interface_info, indent=4)

def main():
   csr = CiscoRestconf('10.254.0.1', username='cisco', password='cisco') 
   print(csr.get_interface_ips(csr.get_interface_info())) 
   with open('csr_interface_IPs.json', 'w') as json_file:
       print(csr.get_interface_ips(csr.get_interface_info()), file=json_file)

if __name__ == '__main__':
   main()