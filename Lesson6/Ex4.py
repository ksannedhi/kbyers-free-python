from netmiko import ConnectHandler
from getpass import getpass

cisco_xe = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = ConnectHandler(**cisco_xe)

print("-" * 60)
print("Before the change:")
print("-" * 60)
cur_op = xe_connect.send_command("sho run | inc logg")
print(cur_op)
print("-" * 60)
print("-" * 60)

cmds = ['logg buff 5000', 'loggi console']
output = xe_connect.send_config_set(cmds)
print(output)

print("-" * 60)
print("-" * 60)
print("After the change:")
print("-" * 60)
new_op = xe_connect.send_command("show run | inc logg")
print(new_op)
print("-" * 60)
print("-" * 60)

file = "log_config.txt"
output = xe_connect.send_config_from_file(file)
print("After config file push:")
print("-" * 60)
print(xe_connect.send_command("show run | inc logg"))
print("-" * 60)
print("-" * 60)
