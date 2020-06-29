show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
dev_details = show_version.split()

print(f'Model is "{dev_details[1]}" & the Serial number is "{dev_details[2]}".')

if "Cisco" in dev_details[1].lower().capitalize():
    print("Cisco is present in the model number.")

if "881" in dev_details[1]:
    print("881 is in the model number.")

#Altenatively
vendor_cisco = 'cisco' in dev_details[1].lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))

model_881 = '881' in dev_details[1]
print("Checking if model contains 881: {}".format(model_881))