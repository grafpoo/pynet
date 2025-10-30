from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

cisco3 = {
    "host": "cisco3.lasthop.io", 
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    # "session_log": "sesh.log",
}
arista1 = {
    "host": "arista1.lasthop.io", 
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    # "session_log": "sesh.log",
}
nx_osv = {
    "host": "nxos1.lasthop.io", 
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    # "session_log": "sesh.log",
}
juniper_srx = {
    "host": "srx2.lasthop.io", 
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    # "session_log": "sesh.log",
}

devices = [cisco3, arista1, nx_osv, juniper_srx]

for device in devices:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    if "cisco" in device["host"]:
        # output = net_connect.send_command("show ip int brief")
        output = net_connect.send_command("show version")
        tempfile = f"{device['host']}_show_version.txt"
        with open(tempfile, "w") as f:
            f.write(output)
    net_connect.disconnect()

