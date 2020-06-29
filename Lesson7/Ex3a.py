import yaml

with open("Ex3a.yml") as f:
    yaml_out = yaml.load(f)

print(yaml_out)
