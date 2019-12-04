def readHTML():
	with open('raw.html', 'r') as file:
		strs = file.read()
		return strs;

import re
pattern = 'r"(?<=mailt).*?(?=style)"'

text = readHTML()

print(re.findall(pattern, text))
