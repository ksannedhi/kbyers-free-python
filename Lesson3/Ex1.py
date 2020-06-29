from pprint import pprint

with open("show_vlan.txt") as f:
    text = f.readlines()

data = text[2:]
data.pop(1)
vlan_details = []
for elem in data:
    vlan_split = elem.split()
    (vlan_id, vlan_name) = (vlan_split[0], vlan_split[1])
    vlan_details.append((vlan_id, vlan_name))

pprint (vlan_details)