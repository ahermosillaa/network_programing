import netmiko
import os

# Guarda comandos swow en directorio roouters por cada equipo

class CiscoIOS():
    """
    This class is designed to connect to a cisco IOS appliance and get various data or 
    issue configuration commands
    """

    def __init__(self, ip, port=22, prompt=False, username=None, 
                        password=None, device_type='cisco_ios'):
        """
        Establishes connection to target device.
        
        :param str ip:              ip address of target device.
        :param int port:            port for connection
        :param str username:        username for authentication
        :param str password:        password for authentication
        :param str device_type:     should not change, class is designed for Cisco IOS
        """
        self.conn = netmiko.ConnectHandler(ip=ip, port=port, username=username,
                        password=password, device_type=device_type)
        _ = self.conn.send_command('sh run | include hostname')
        self.hostname = _.split()[-1]

    def get_run_cfg(self):
        """
        Returns the running-config from the appliance as a string
        """
        running_config = self.conn.send_command('sh run')
        return running_config

    def get_ip_int(self):
        """
        Returns the output from show ip interface as a string
        """
        ip_int = self.conn.send_command('sh ip int')
        return ip_int

    def get_log(self):
        """
        Returns the log from the appliance as a string
        """
        log = self.conn.send_command('sh log')
        return log

def main():
    #print(os.getcwd())
    ip_list = [
        '10.254.0.1',
        '10.254.0.2',
        '10.254.0.3',
    ]
    router_list = []
    for ip in ip_list:
        conn = CiscoIOS(ip, username='cisco', password='cisco') 
        router_list.append(conn)
    for router in router_list:
        base_dir = os.getcwd() + '/routers/' 
        router_dir = base_dir + router.hostname + '/'
        os.mkdir(router_dir)
        data_dict = {
            'running-config': router.get_run_cfg(), 
            'ip-interface': router.get_ip_int(), 
            'log': router.get_log(), 
        }
        for output in data_dict:
            filename = router_dir + output + '.txt'
            with open(filename, 'w') as f: 
                print(data_dict[output], file=f)

if __name__ == '__main__':
    main()
    for _ in os.walk('routers'): 
        print(_)