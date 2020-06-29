import jinja2

networks = ["10.100.201.0/24", "10.100.202.0/24", "10.100.203.0/24"]

bgp_var_dict = {"local_as": 10, "neighbor_ip": "10.100.200.5", "remote_as": 20,
                "advt_routes": networks}

with open("bgp_temp2.txt") as f:
    bgp_temp = f.read()

t = jinja2.Template(bgp_temp)
print(t.render(bgp_var_dict))