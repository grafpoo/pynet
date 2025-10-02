from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": "cisco1.lasthop.io", 
    "username": "john_guthrie",
    "password": getpass(), 
    "device_type": "cisco_ios",
    # "session_log": "sesh.log",
}
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
net_connect.disconnect()
