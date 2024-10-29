import netmiko

class cisco():
    
    
    def __init(self, ip, device_type=None, username=None, password=None):

        self.conn_data = {
            'ip' : ip,
            'device_type' : device_type,
            'username' : username,
            'password' : password
        }

    def login(self): 

        return netmiko.ConnectHandler(**self.conn_data)


class ciscoIOS(cisco):
    
    
    def __init__(self, ip, username=None, password=None):

        self.conn_data = {
            'ip' : ip,
            'device_type' : 'cisco_ios',
            'username' : username,
            'password' : password
        }

    def login(self):
        
        return super().login()

    def populate_interface_list(self):

        conn = self.login()
        ip_int_br = conn.send_command('sh ip int br', use_textfsm=True)
        self.interface_list = []
        for interface in ip_int_br:
            self.interface_list.append(interface['intf'])

def main():
    csr1vk1 = ciscoIOS('10.254.0.1', username='cisco', password='cisco')
    csr1vk1.populate_interface_list()
    print(csr1vk1.interface_list)

if __name__ == '__main__':
    main()