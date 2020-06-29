from netmiko import ConnectHandler
from getpass import getpass

cisco_xe = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = ConnectHandler(**cisco_xe)
file = "test9.txt"
cmd = "delete flash:{}".format(file)

file_del_op = xe_connect.send_command_timing(cmd, strip_command=False, strip_prompt=False)

if file in file_del_op:
    file_del_op += xe_connect.send_command_timing("\n")
    file_del_op += xe_connect.send_command_timing("\n")

xe_connect.disconnect()
print(file_del_op)
