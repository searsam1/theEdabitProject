import re

def security(txt):
	pattern = "T[x]*\$|\$[x]*T"
	match = re.search(pattern, txt)
	return ["Safe","ALARM!"][bool(match)]

print(
	security("xxxxTTxGxx$xxTxxx")
	)
