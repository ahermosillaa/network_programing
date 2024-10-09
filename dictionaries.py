import netmiko 

csr1kv1_connection_info = {
    'ip' : '10.254.0.1',
    'device_type' : 'cisco_ios',
    'username' : 'cisco',
    'password' : 'cisco',
    'port' : 22
}

#net_connect = netmiko.ConnectHandler( 
#    ip=csr1kv1_connection_info['ip'],  
#    device_type=csr1kv1_connection_info['device_type'], 
#    username=csr1kv1_connection_info['username'],  
#    password=csr1kv1_connection_info['password'],  
#    port=csr1kv1_connection_info['port']) 

# Conesta liena igual funciona la llamada la componente de red

net_connect = netmiko.ConnectHandler(**csr1kv1_connection_info)

print(net_connect.send_command('show run'))