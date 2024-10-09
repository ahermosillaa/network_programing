import netmiko

last_octet = 1
while last_octet <= 3:
    #if last_octet == 1:
    #    last_octet += 1 
        #continue 
        #print('While loop exited with break statement')
        #break
    ip_address = '10.254.0.' + str(last_octet) 
    #print(ip_address)  
    net_connect = netmiko.ConnectHandler(
        ip = ip_address,
        device_type = 'cisco_ios',  
        username = 'cisco',  
        password = 'cisco'  
    )
    print(net_connect.send_command('sh run | include hostname'))
    print( '_' * 20 )
    last_octet += 1  