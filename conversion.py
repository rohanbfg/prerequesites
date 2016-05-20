import sys

print"enter a number in decimal"
decimal=input()
print"to which number system do you wish to convert the number?"
print"for binary type 2:octal type 8"
x=input()
j=0
binary=0
while (decimal>0):
	binary = binary+((10**(j))*(decimal%x))
	decimal=decimal/x
	j=j+1
if(x==2):
	print"the equivalent binary number is,",binary
else:
	print"the equivalent octal number is,",binary

