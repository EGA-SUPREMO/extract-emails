def readJSON():
	with open('eu', 'r') as json_file:
		str_json = json_file.read()
		data = str_json
		return data;

import re
pattern = 'r"(?<=href).*?(?=style)"'

text = readJSON()

print(re.findall(r"(?<=mailto).*?(?=style)", text))
#for i in matches:
	#print(i)