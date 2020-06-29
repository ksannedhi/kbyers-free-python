f = open("show_version.txt")
text = f.read()
print(text)
print(type(text))
f.close()

print("-" * 60)

with open("show_version.txt") as f:
    text = f.readlines()
print(text)
print(type(text))
