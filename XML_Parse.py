#!/usr/bin/python
import xml.etree.ElementTree as ET
i = 0;
titles = {}
tree = ET.parse('/Users/aram/Documents/Code/list.xml')
root = tree.getroot()
for child in root:
	id = child.attrib.get("id")
	print id
	for child in child:
		while i < 1:
			print child.text
			i = i + 1
	i = 0
	print "\n"
print titles
