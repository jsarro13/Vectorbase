import codecs
#open it with utf-8 encoding 
f=codecs.open("R_FranklinCty2007_out.csv","r",encoding='utf-8')
#read the file to unicode string
sfile=f.read()

#check the encoding type
print type(file) #it's unicode

#unicode should be encoded to standard string to display it properly
print sfile.encode('utf-8')
#check the type of encoded string

print type(sfile.encode('utf-8'))
