import sys
print "enter a number in binary.PLEASE put a SPACE after each digit."
list= map(int, raw_input().split()) 
x=0
l=[]
list.reverse()
while(x<(len(list))):
	j=0
	octal=0
	if((x+3)<len(list)):
		for m in range (x,x+3):
			octal=octal+list[m]*(2**(j))
			m=m+1
			j=j+1
	else:
		for m in range (x,len(list)):
			octal=octal+list[m]*(2**(j))
			m=m+1
			j=j+1
	l.append(octal)
	x=x+3
l.reverse()
print "the equivalent octal number is:    "

print ''.join(map(str, l))