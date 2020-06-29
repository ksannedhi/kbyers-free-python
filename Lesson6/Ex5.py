from netmiko import ConnectHandler
from getpass import getpass

cisco_xe = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = ConnectHandler(**cisco_xe)
normal_op = xe_connect.send_command("show ip ar")
print(normal_op)

with_textfsm = xe_connect.send_command("show ip arp", use_textfsm=True)
print(with_textfsm)
