import yaml, jinja2

with open("Ex3b.yml") as f:
    intf_vars = yaml.load(f)

intf_temp = '''
{%- for intf_name, intf_dict in interfaces.items() %}
interface {{ intf_name }}
  {%- if intf_dict.mode == 'access' %}
  switchport mode access
  switchport access vlan {{ intf_dict.vlan }}
  {%- else %}
  switchport mode trunk
  switchport trunk native vlan {{ intf_dict.native_vlan }}
  switchport trunk allowed vlan {{ intf_dict.trunk_vlans }}
  {%- endif %}
{%- endfor %}
'''

t = jinja2.Template(intf_temp)
print(t.render(intf_vars))

