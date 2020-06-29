from netmiko import Netmiko
from getpass import getpass

cisco_xe = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = Netmiko(**cisco_xe)

dev_prompt = xe_connect.find_prompt()
print(dev_prompt)
