import jinja2

vlan_dict = {"501": "blue501", "502": "blue502", "503": "blue503", "504": "blue504", "505": "blue505", "506": "blue506", "507": "blue507", "508": "blue508"}

vlan_data = {"vlans": vlan_dict}

vlan_temp = '''
{%- for vlan_id, vlan_name in vlans.items() %}
vlan {{vlan_id}}
    name {{vlan_name}}
{%- endfor %}
'''

t = jinja2.Template(vlan_temp)
print(t.render(vlan_data))
