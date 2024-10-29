import netmiko

#ip_list = []

def populate_ip_list(ip_base, ip_range):
    ip_list = []
    for n in ip_range:
        ip_addr = ip_base + str(n)
        ip_list.append(ip_addr)
    return ip_list

# ip_list = populate_ip_list('10.0.0.', range(1,33))
# print(ip_list)

def get_ios_output(ip_list, command):
    for ip in ip_list:
        net_connect = netmiko.ConnectHandler(ip=ip, device_type='cisco_ios',
            username='cisco', password='cisco', port=22)
        print(net_connect.send_command(command))

ip_list = populate_ip_list('10.254.0.', range(1,4))
get_ios_output(ip_list, 'sh ip int br')