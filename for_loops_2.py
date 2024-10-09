import routers

for router in routers.creds:
   print(routers.get_ip_int_br(**router))
   print('-' * 80)