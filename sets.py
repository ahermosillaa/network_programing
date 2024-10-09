import netmiko 
 
ip_addrs = [ 
    '10.254.0.1', 
    '10.254.0.2', 
    '10.254.0.1', 
    '10.254.0.3', 
    '10.254.0.2', 
    '10.254.0.3', 
    '10.254.0.3', 
    '10.254.0.2', 
    '10.254.0.3', 
]

ip_addrs_unique = set(ip_addrs)
print(ip_addrs_unique)