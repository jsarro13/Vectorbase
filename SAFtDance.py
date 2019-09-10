#/usr/bin/python
#SAFtDance v1 04-10-2019
#Written by Joseph Sarro
#This script splits trap data when multiple species are in 1 row
#To run enter filenames for f and G below as well as x and y ranges. On command line: python SAFtDance.py. You can also dance if you want to and leave your friends behind.
#Last edit 04-11-2019
#files to be opened and written.  F needs to be changed to match your .txt file before running as does datafile below.  
import os
f = open('2017_full_Data.txt', 'r')
G= open('SAF_2017.out..test.txt','w')
#read in header file to save and print species names later
line = f.readline()
field=line.split("	")
header=field[0]
#print header
#name=field[73]
#print name
#Print the header
for y in range(0,13):
	print >> G, field[y],"	",
print >> G, "species","	","sample_count"
#Read rest of file and begin splitting 
#for i in xrange(1):
#	f.next()
curline=1
for lines in f:
	curline +=1
	#print curline
	fields = lines.split("	")
	sq=fields[0]
	#print sq
	any=False
	for x in range(13, 17):
		#print x
		#if fields[x] is None:
		#	print x
		#	exit()
		cur=fields[x]
		#print cur
		if cur == "#@": #Note I used #@ as a unique identifier to deal with blank cells. THis can be changed to anything.
			pass
		elif int(cur) > 0:
			any = True
			species=field[x]
			for y in range(0,13):
				print >> G, fields[y],"	",
			print >> G, species,"	",cur
			print species+cur
	if any == False:
		for y in range(0,13):
                                print >> G, fields[y],"	",
		print >> G, "BLANK","	",0
	#print lines	
G.close()
