import re,urllib

url = "http://www.pythonchallenge.com/pc/def/equality.html"
source = urllib.urlopen(url).read()

print ''.join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",source))