import jinja2

bgp_vars = {"local_as": 10, "neighbor_ip": "192.168.20.3", "remote_as": 20}

temp_file = "C:\\Users\\kalyana.sannedhi\\PycharmProjects\\Lesson8\\bgp_template.j2"
with open(temp_file) as f:
    bgp_temp = f.read()

t = jinja2.Template(bgp_temp)
print(t.render(bgp_vars))
