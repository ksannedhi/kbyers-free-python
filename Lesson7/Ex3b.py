import yaml
from pprint import pprint

with open("Ex3b.yml") as f:
    yaml_out = yaml.load(f)

pprint(yaml_out)
