#!/usr/bin/python

from urllib2 import urlopen
import xml.etree.ElementTree as ET
z = 0;

url = 'http://api.npr.org/list?id=3002'
xmlOut = urlopen(url)
final = xmlOut.read()
f = open('xmlOut1.xml', 'w')
f.write(final)
f.close()
i = 0;
titles = {}
tree = ET.parse('/Users/aram/Documents/Code/xmlOut1.xml')
root = tree.getroot()
for child in root:
	id = child.attrib.get("id")
	print id
	for child in child:
		while i < 1:
			titles[child.text] = id
			i = i + 1
		
	
	i = 0
	print "\n"
f2 = open('programOut.txt', 'w')
f2.write(str(titles))
f2.close()
print titles
