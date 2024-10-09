import pandas
import cisco1 

with open('router_info.csv') as csv_file: 
    df = pandas.read_csv(csv_file) 
#print(df)
#print(df['ip']) 
#print(df.loc[[0]])

router_list = []
version_list = []

for index, row in df.iterrows():
    router = cisco1.CiscoIOS (  
        row['ip'], 
        username=row['username'],  
        password=row['password'], 
        port=row['port'], 
        device_type=row['device_type'] 
    )
    version_data = router.get_IOS_version() 
    hostname = version_data['hostname'] 
    version = f"{version_data['rommon']} {version_data['version']}"

    router_list.append(hostname)
    version_list.append(version)

#print(router_list, version_list, sep='\n')

router_data = pandas.DataFrame() 
router_data['hostname'] = router_list 
router_data['version'] = version_list 

#print(router_data)
router_data.to_csv('hostname_version.csv', index=False)