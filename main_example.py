import netmiko

def main():

    csr = netmiko.ConnectHandler(
    '10.254.0.1', 
    username='cisco', 
    password='cisco',
    device_type='cisco_ios'
    )
    print(csr.send_command('sh ip route'))

if __name__ == '__main__':
    main()