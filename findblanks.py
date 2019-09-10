#/usr/bin/python
#findblanks v1 08-2019
#Written by Joseph Sarro
#This script looks for traps that contain blank data 
#files to be opened and written.  F needs to be changed to match your .txt file before running as does datafile below.  
import os
#f = open('blanks.csv', 'r')
#f2-= open('noblanks.csv', 'r')
#G= open('SAF_2017.out.txt','w')
#read in header file to save and print species names later
#line = f.readline()
#line2=f2.readline()
#field=line.split(",")
#field2=line2.split(",")


datafile = file('blanks.csv')
#datafile2 = file('noblanks.csv')
for line in datafile:
        field=line.split(",")   
        start=field[2]
        lat=field[3]
	lon=field[4]
	sp=field[8]
        there=False
	datafile2 = file('noblanks.csv')
	for line2 in datafile2:
		field2=line2.split(",")
       		start2=field2[2]
       		lat2=field2[3]
       		lon2=field2[4]		
		sp2=field2[8]
		#print sp2
	       	#print start2,",",lat2,",",lon2
		#print start,start2
		if start == start2 and lat == lat2 and lon == lon2 and sp == sp2:
			there = True
			print start,",",lat,",",lon
	#if there == False:
	#	print start,",",lat,",",lon       
