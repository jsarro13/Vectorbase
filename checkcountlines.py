#/usr/bin/python
#08-2019
#Written by Joseph Sarro
#This script adds trap data counts for single traps. If the number is less that the total trap count, an new data line is added with the remaining value with a stop marker.
import os
#f = open('blanks.csv', 'r')
#f2-= open('noblanks.csv', 'r')
G= open('headout.csv','w')
#read in header file to save and print species names later
#line = f.readline()
#line2=f2.readline()
#field=line.split(",")
#field2=line2.split(",")

prevstart = "BLANK"
prevlat = "BLANK"
prevlon = "BLANK"
prevtrap = "BLANK"
totalcount = "BLANK"
curcount = 0
zero =""
one =""
two =""
three =""
four =""
five =""
six =""
seven =""
eight =""
nine =""
ten =""
eleven =""
twelve =""
thirteen =""
fourteen =""
fifteen =""
sixteen =""
seventeen =""
eighteen =""
nineteen =""
twenty =""
twentone =""
twentytwo =""
twentythree =""
twentyfour =""
previd =""
#datafile = file('poolout.csv')
datafile = file('joined5.splitV.csv')
#datafile2 = file('noblanks.csv')
for line in datafile:
        field=line.split(",")   
        start=field[4]
        lat=field[6]
	lon=field[7]
	trap=field[13]
	id=field[0]
	if previd != id and prevstart == start and prevlat == lat and prevlon == lon and prevtrap == trap:
		blue="blue"
		#print  zero,",",one,",",two,",",three,",",four,",",five,",",six,",",seven,",",eight,",",nine,",",ten,",",eleven,",",twelve,",",thirteen,",",fourteen,",",fifteen,",",sixteen,",",seventeen,",",eighteen,",",nineteen,",",twenty,",",twentone,",",twentytwo,",",twentythree,",",",",",stop",","
                #print  field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],",marker"
	if prevstart == "BLANK":
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","
		prevstart = start
		prevlat = lat
		prevlon = lon
		prevtrap = trap
		previd = id
		totalcount = field[16]
		curcount = int(field[24])
	elif prevstart == start and prevlat == lat and prevlon == lon and prevtrap == trap:
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","	
		curcount = curcount + int(field[24])
		previd = id
	else:
		if int(totalcount) == curcount:
			print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","
		else:
			diffcount=int(totalcount)-curcount
			#print prevstart,",",five,",",six,",",seven,",",eight,",",nine,",",ten
			print >> G, zero,",",one,",",two,",",three,",",four,",",five,",",six,",",seven,",",eight,",",nine,",",ten,",",eleven,",",twelve,",",thirteen,",",fourteen,",",fifteen,",",sixteen,",",seventeen,",",eighteen,",",nineteen,",",twenty,",",twentone,",",twentytwo,",",",","stop",diffcount,","
			print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","
		prevstart = start
                prevlat = lat
                prevlon = lon
                prevtrap = trap
		previd = id
		totalcount = field[16]
		curcount = int(field[24])
		zero=field[0]
		one =field[1]
		two =field[2]
		three =field[3]
		four =field[4]
		five =field[5]
		six =field[6]
		seven =field[7]
		eight =field[8]
		nine =field[9]
		ten =field[10]
		eleven =field[11]
		twelve =field[12]
		thirteen =field[13]
		fourteen =field[14]
		fifteen =field[15]
		sixteen =field[16]
		seventeen =field[17]
		eighteen =field[18]
		nineteen =field[19]
		twenty =field[20]
		twentone =field[21]
		twentytwo =field[22]
		twentythree =field[23]
		twentyfour = field[24]
