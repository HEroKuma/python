import re,urllib,string

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

source = urllib.urlopen(url).read()
str = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(source)[-1]

char = []
data = list(str)

for i in range(len(data)):
	if (65 <= ord(data[i]) <= 90) or (97 <= ord(data[i]) <= 122):
		char.append(data[i])
		
text = ''.join(char)
print text