import netmiko

ip_list = [
    '10.254.0.1',
    '10.254.0.2',
    '10.254.0.3',
]
#print(ip_list[0])
#print(ip_list[-1])

username = 'cisco' 
password = 'cisco' 
device_type = 'cisco_ios' 
port = 22 

output_list = []    

for ip in ip_list:
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type, 
        username=username, password=password, port=port)
    output = net_connect.send_command('show ip interface brief')
    output_list.append(output)

for output in output_list:
    print(output)