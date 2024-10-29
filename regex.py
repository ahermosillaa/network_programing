import netmiko
import re

ip = '10.254.0.1'
username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
    username=username, password=password, port=port)
csr1kv1_ip_int_br = net_connect.send_command('sh ip int br')
#print(csr1kv1_ip_int_br)
#print(type(csr1kv1_ip_int_br))

sh_ip_int_split = re.split(r'\n', csr1kv1_ip_int_br)
#print(sh_ip_int_split)

regex_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
ip_string = str()

for value in sh_ip_int_split:
    ip = re.search(regex_pattern, value)
    if ip:
        ip_string += ip.group(0) + ','

print(ip_string)
