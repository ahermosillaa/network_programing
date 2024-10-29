import netmiko
import re

ip = '10.254.0.1'
username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
    username=username, password=password, port=port)
csr1kv1_ip_int_br = net_connect.send_command('show ip interface brief')

#ip_addr = re.search(r'\w+\s+([\d\.]+)', csr1kv1_ip_int_br)
#print(ip_addr.group(1))

#ip_addr = re.findall(r'\w+\s+([\d\.]+)', csr1kv1_ip_int_br)
#print(ip_addr)

re_pattern = r'(GigabitEthernet1.*)'
gigabit_ethernet_1 = re.search(re_pattern, csr1kv1_ip_int_br)
print(gigabit_ethernet_1.group(1))