with open("show_lldp_neighbors_detail.txt") as f:
    text = f.read()

lldp_text = text.splitlines()
lldp_text.pop(0)

for elem in lldp_text:
    lldp_details = elem.split(":")
    parameter = lldp_details[0]
    value = lldp_details[1]
    if parameter == "Port id":
        port_id = value
    elif parameter != "System Name":
        continue
    else:
        sys_name = value
        break

print(sys_name, port_id)

sys_name, port_id = (None, None)

for line in text.splitlines():
    if 'System Name: ' in line:
        _, sys_name = line.split("System Name: ")
    elif "Port id: " in line:
        _, port_id = line.split("Port id: ")

    if sys_name and port_id:
        break

print()
print("System name is", sys_name)
print("Port ID is", port_id)