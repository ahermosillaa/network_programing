import netmiko
import re

csr = netmiko.ConnectHandler('10.254.0.1', username='cisco',
   password='cisco', device_type='cisco_ios')

running_config = csr.send_command('show run')
# print(running_config)

pattern = r'interface GigabitEthernet1\n.+'
repl = 'interface GigabitEthernet1\n ip address 10.11.0.1 255.255.255.0'
updated_config = re.sub(pattern, repl, running_config)
#print(updated_config)

with open('csr1kv1.cfg', 'w') as config_file:
    print(updated_config, file=config_file)