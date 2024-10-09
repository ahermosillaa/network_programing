import netmiko
import pprint

username = 'cisco' 
password = 'cisco' 
device_type = 'cisco_ios' 
port = 22 

ip_tuple = (
    '10.254.0.1',
    '10.254.0.2',
    '10.254.0.3',
)

output_list = []
for ip in ip_tuple:
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, 
        username=username, password=password, port=port) 
    hostname = net_connect.send_command(
        'sh run | include hostname'
    ).strip() 
    ios_xe_version = net_connect.send_command(
        'sh version | section Cisco IOS XE Software, Version'
    ).strip()
    output_tuple = (hostname, ios_xe_version)
    output_list.append(output_tuple)

pprint.pprint(output_list)