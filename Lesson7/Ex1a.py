import jinja2

vlan_vars = {"vlan_id": 500, "vlan_name": "red500"}

vlan_temp = '''
vlan {{vlan_id}}
    name {{vlan_name}}
'''

t = jinja2.Template(vlan_temp)
print(t.render(vlan_vars))

