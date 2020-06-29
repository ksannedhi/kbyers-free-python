import jinja2

ospf_vars = {"ospf_process_id": 10, "ospf_priority": 100, "ospf_active_interface1": "Vlan1", "ospf_active_interface2": "Vlan2",
            "advt_routes": ['10.10.10.0/24', '10.10.20.0/24', '10.10.30.0/24']}

with open("ospf_temp.j2") as f:
    ospf_temp = f.read()

t = jinja2.Template(ospf_temp)
print(t.render(ospf_vars))

