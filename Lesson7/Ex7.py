import jinja2, csv

with open("bgp_vars.csv") as f:
    read_csv = csv.DictReader(f)
    for bgp_variables in read_csv:
        advt_routes = bgp_variables["advt_routes"]
        advt_routes = advt_routes.split()
        bgp_variables["advt_routes"] = advt_routes

        with open("bgp_temp3.j2") as f:
            bgp_temp = f.read()

        t = jinja2.Template(bgp_temp)
        print(t.render(bgp_variables))
        print("-" * 60)