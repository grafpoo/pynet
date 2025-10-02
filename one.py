from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host="cisco1.lasthop.io", 
    username="john_guthrie",
    password=getpass(), 
    device_type="cisco_ios",
    session_log="sesh.log",
    )
print(net_connect.find_prompt())
net_connect.disconnect()
