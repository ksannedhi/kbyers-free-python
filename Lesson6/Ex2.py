from netmiko import Netmiko
from getpass import getpass

cisco_xe = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = Netmiko(**cisco_xe)

output = xe_connect.send_command("sh ip int br")
print(output)
