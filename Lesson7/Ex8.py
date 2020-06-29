import jinja2

net_vars = {
            "routers": {"routeA": "10.10.10.5", "routerB": "10.10.10.20", "routerC": "10.10.10.15"},
            'ips': ['192.168.10.1', '192.168.20.1', '192.168.30.2'],
            "ipv6_enabled": True,
            "ipv4_enabled": True
            }

net_temp = """
{%- for router, network in routers.items() %}
{{router}} >>> {{network}}
    {%- for network in ips %}
        {{network}}
    {%- endfor %}
{%- endfor %}

{%- if ipv6_enabled %}
ipv6 enabled
{%- if ipv4_enabled %}
ipv4 enabled
{%- endif %}
{%- endif %}
"""

t = jinja2.Template(net_temp)
print(t.render(net_vars))

net2_vars = {"routes2": {"routeA": "10.10.10.0/24", "routeB": "172.16.20.0/24", "routeC": "192.168.50.0/24"},
             "networks2": ["50.50.50.0/24", "60.60.60.0/24"], "ipv6_addr2": True, "ipv4_addr2": True}

net2_temp = """
{%- for route, network in routes2.items() %}
{{route}} --->>> {{network}}
{%- for network in networks2 %}
{{network}}
{%- endfor %}
{%- endfor %}

{%- if ipv6_addr2 %}
ipv6 is enabled
    {%- if ipv4_addr2 %}
    --->> ipv4 is enabled
    {%- endif %}
{%- endif %}
"""

t2 = jinja2.Template(net2_temp)
print(t2.render(net2_vars))
