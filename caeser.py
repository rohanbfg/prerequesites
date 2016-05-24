import sys
print "enter a string followed by two numbers separated by spaces. The first number should be 0 or 1"
caesar=[]
final=[]
item =raw_input()
caesar=item.split()
if int(caesar[1])==1:
	for x in caesar[0]:
		x=chr(ord(x)+int(caesar[2]))
		final.append(x)
elif int(caesar[1])==0:
	for x in caesar[0]:
		x=chr(ord(x)-int(caesar[2]))
		final.append(x)
print ''.join(map(str, final))
