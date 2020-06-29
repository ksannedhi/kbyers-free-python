import jinja2

networks = ["10.200.201.0/24", "10.200.202.0/24", "10.200.203.0/24"]

bgp_var_dict = {"local_as": 10, "neighbor_ip": "10.200.200.5", "neighbor_as": 20,
                "advt_routes": networks, "ipv6_addr": True}

with open("bgp_temp3.j2") as f:
    bgp_temp = f.read()

t = jinja2.Template(bgp_temp)
print(t.render(bgp_var_dict))