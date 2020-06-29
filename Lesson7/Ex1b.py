import jinja2

isakmp_vars = {"isakmp_enabled": True, "enc_type": "aes", "group_id": 7}

isakmp_temp = '''
{%- if isakmp_enabled %}
crypto isakmp policy 10
 encr {{enc_type}}
 authentication pre-share
 group {{group_id}}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{%- endif %}
'''

t = jinja2.Template(isakmp_temp)
print(t.render(isakmp_vars))

