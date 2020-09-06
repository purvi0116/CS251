# Enter your code here
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-m","--mes_file",dest="file")

args = parser.parse_args()


with open(args.file) as file_object:
	lines = file_object.readlines()

N = int(lines[0])

y=re.findall('\$\((.+?\)#\(.+?)\)\$',lines[1])
a=[]

corrupt=0
for i in range(0,len(y)):
	
	if(corrupt):
		break
	flag = 1  #flag for confirming that this seq is indeed a valid valid
	corrupt=0
	a = y[i].split(')#(')
	x1=a[0].split(',')
	x2=a[1].split(',')
	
	sum1=0
	sum2=0
	for jj in range(0,len(x1)):
		if not x1[jj].isdecimal():
			
			flag=0
			break
			
				
	if (flag):
		for jj in range(0,len(x2)):
			if not x2[jj].isdecimal():
				flag=0
				break		

	if(flag):
		for jj in range(0,len(x1)):
			if int(x1[jj])>=N:
				corrupt=1
				break
			sum1+=(jj+1)*int(x1[jj])
		if(sum1%N!=0):
			corrupt=1
		if corrupt==0:	
			for jj in range(0,len(x2)):
				if int(x2[jj])>=N:
					corrupt=1
					break
				sum2+=(jj+1)*int(x2[jj])
			
			if(sum2%N!=0):
				corrupt=1	
			
if(corrupt):
	print("CORRUPTED")
else:
	print("OK")		
				