import re

with open("show_version.txt") as f:
    text = f.read()

ver = re.search(r'^Cisco .* Version (\S+),', text, flags=re.M).group(1) #See the proc below. No need for ? here as it is the last , in this line.
ser = re.search(r'Processor board ID (.*)\s', text, flags=re.M).group(1)
reg = re.search(r'^.* register is (\w+)\n', text, flags=re.M).group(1)
proc = re.search(r'^.*Cisco 881 (.*?)\s', text, flags=re.M).group(1) #Don't give space before "Cisco" & notice ? to stop the greediness.
proc_wo_braces = re.search(r'Cisco 881 \((\S+)\)', text, flags=re.M).group(1)

print("OS Version:", ver)
print("Serial Number:", ser)
print("​Config Register:", reg)
print("Processor:", proc)
print("Processor:", proc_wo_braces)
