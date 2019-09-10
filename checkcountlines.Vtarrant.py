#/usr/bin/python
#09-2019
#Written by Joseph Sarro
#This script checks that pathogen data counts total the trap number count for tarrant county 2018 data. If it does not, it generates a new line with remaining counts.
import os
G= open('virus.formatted.csv','w')
datafile = file('virus.csv')
for line in datafile:
        field=line.split(",")   
        total=int(field[5])
        numbertested=int(field[6])
	if total-numbertested ==0:
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8].rstrip("\n")
	elif total-numbertested >0:
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8].rstrip("\n")
		print >> G, field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",",",int(total-numbertested),",,"
	else:
		print field[0],",",field[1],",",field[2],",",field[3],",",field[4],",",field[5],",",field[6],",",field[7],",",field[8].rstrip("\n")
G.close()
