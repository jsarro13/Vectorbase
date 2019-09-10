#/usr/bin/python
#08-2019
#Written by Joseph Sarro
#This script pools trap data for RAMP or LAMP tests with a matching RTPCR test. If the trap has any samples left over, a non-pathogen sample is added with the left over count.
import os
#f = open('blanks.csv', 'r')
#f2-= open('noblanks.csv', 'r')
G= open('poolout.csv','w')
#read in header file to save and print species names later
#line = f.readline()
#line2=f2.readline()
#field=line.split(",")
#field2=line2.split(",")

zero ="BLANK"
one ="BLANK"
two ="BLANK"
three ="BLANK"
four ="BLANK"
five ="BLANK"
six ="BLANK"
seven ="BLANK"
eight ="BLANK"
nine ="BLANK"
ten ="BLANK"
eleven ="BLANK"
twelve ="BLANK"
thirteen ="BLANK"
fourteen ="BLANK"
fifteen ="BLANK"
sixteen ="BLANK"
seventeen ="BLANK"
eighteen ="BLANK"
nineteen ="BLANK"
twenty ="BLANK"
twentone ="BLANK"
twentytwo ="BLANK"
twentythree ="BLANK"
twentyfour ="BLANK"
#datafile = file('tester')
datafile = file('joined5.splitV.csv')
#datafile2 = file('noblanks.csv')
for line in datafile:
        field=line.split(",")   
        start=field[4]
        lat=field[6]
	lon=field[7]
	trap=field[13]
	id=field[0]
        virus=field[23]
	num=field[24]	

	if four == "BLANK" and ("RAMP" in virus or "LAMP" in virus):
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

	elif four == "BLANK":
                print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","
	
	elif four == start and six == lat and seven == lon and thirteen == trap and "RT" in virus and twentyfour == num:	
		print >> G, zero,",",one,",",two,",",three,",",four,",",five,",",six,",",seven,",",eight,",",nine,",",ten,",",eleven,",",twelve,",",thirteen,",",fourteen,",",fifteen,",",sixteen,",",seventeen,",",eighteen,",",nineteen,",",twenty,",",twentone,",",twentytwo,",",twentythree,"|",virus,",",twentyfour,","
		zero ="BLANK"
		one ="BLANK"
		two ="BLANK"
		three ="BLANK"
		four ="BLANK"
		five ="BLANK"
		six ="BLANK"
		seven ="BLANK"
		eight ="BLANK"
		nine ="BLANK"
		ten ="BLANK"
		eleven ="BLANK"
		twelve ="BLANK"
		thirteen ="BLANK"
		fourteen ="BLANK"
		fifteen ="BLANK"
		sixteen ="BLANK"
		seventeen ="BLANK"
		eighteen ="BLANK"
		nineteen ="BLANK"
		twenty ="BLANK"
		twentone ="BLANK"
		twentytwo ="BLANK"
		twentythree ="BLANK"
		twentyfour ="BLANK"

	elif four == start and six == lat and seven == lon and thirteen == trap and "RT" in virus and twentyfour != num:
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","

	elif "RAMP" in virus or "LAMP" in virus:
		print zero,",",one,",",two,",",three,",",four,",",five,",",six,",",seven,",",eight,",",nine,",",ten,",",eleven,",",twelve,",",thirteen,",",fourteen,",",fifteen,",",sixteen,",",seventeen,",",eighteen,",",nineteen,",",twenty,",",twentone,",",twentytwo,",",twentythree,",",twentyfour,","
		print >> G, zero,",",one,",",two,",",three,",",four,",",five,",",six,",",seven,",",eight,",",nine,",",ten,",",eleven,",",twelve,",",thirteen,",",fourteen,",",fifteen,",",sixteen,",",seventeen,",",eighteen,",",nineteen,",",twenty,",",twentone,",",twentytwo,",",twentythree,",",twentyfour,","
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

	else:
		print >> G, zero,",",one,",",two,",",three,",",four,",",five,",",six,",",seven,",",eight,",",nine,",",ten,",",eleven,",",twelve,",",thirteen,",",fourteen,",",fifteen,",",sixteen,",",seventeen,",",eighteen,",",nineteen,",",twenty,",",twentone,",",twentytwo,",",twentythree,",",twentyfour,","
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8],",",field[9],",",field[10],",",field[11],",",field[12],",",field[13],",",field[14],",",field[15],",",field[16],",",field[17],",",field[18],",",field[19],",",field[20],",",field[21],",",field[22],",",field[23],",",field[24],","
		zero ="BLANK"
                one ="BLANK"
                two ="BLANK"
                three ="BLANK"
                four ="BLANK"
                five ="BLANK"
                six ="BLANK"
                seven ="BLANK"
                eight ="BLANK"
                nine ="BLANK"
                ten ="BLANK"
                eleven ="BLANK"
                twelve ="BLANK"
                thirteen ="BLANK"
                fourteen ="BLANK"
                fifteen ="BLANK"
                sixteen ="BLANK"
                seventeen ="BLANK"
                eighteen ="BLANK"
                nineteen ="BLANK"
                twenty ="BLANK"
                twentone ="BLANK"
                twentytwo ="BLANK"
                twentythree ="BLANK"
                twentyfour ="BLANK"

G.close()
