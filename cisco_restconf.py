import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup

def get_interface_info(to_terminal=False):
    """ 
    Returns interface information in XML format 
    If to_terminal=True prints data instead of returning
    """
    api_root = 'https://10.254.0.1:443/restconf' 
    dn = '/data/Cisco-IOS-XE-native:native/interface/'

    response = requests.get(api_root + dn, 
    auth=('cisco', 'cisco'), 
    verify=False
    )

    if to_terminal == True:
        print(response.content.decode('utf-8'))
    else:
        return response.content

#get_interface_info(to_terminal=True)
xml_data = get_interface_info()
soup = BeautifulSoup(xml_data, 'lxml')
#print(soup.prettify())
#print(soup.gigabitethernet)
for intf in soup.find_all('gigabitethernet'): 
    #print(intf.name + intf.find('name').string)
    #print('-' * 50)
    print('-' * 25)
    ip = intf.find('ip')
    if ip:
        print('GigabitEthernet', intf.find('name').string)  
        print(intf.ip.primary.address)