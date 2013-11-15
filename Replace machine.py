


letterdict = {'a':'a', : 'b':'be', 'c':'ce', 'd':'de', 'e':'e', 'f':'efe', 'g':'ge', 'h':'hache', 'i':'i', 'j':'jota', 'k':'ka', 'l':'ele', 'm':'eme','n':'ene', 'o':'o', 'p':'pe', 'q':'cu', 'r':'ere', 's':'ese', 't':'te', 'u':'u', 'v':'ve', 'w':'doble ve', 'x':'equis', 'y':'i griega', 'z':'zeta'}
writeBuffer[0] = ''
readFile = open("./SpanWords.txt", "r")
writeFile = open("./SpanSpell.txt", "w")
for line in readFile:
  i=0
  writeBuffer[:] = []
  for letter in line:
    writeBuffer[i] = letterdict.get(letter, default=None)
  for item in writeBuffer:
    writeFile.write(item + ' ')
  writeFile.write('\n')
  i=i+1
  
