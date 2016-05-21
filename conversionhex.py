import sys

print"enter a number in decimal"
decimal=int(raw_input())
list=[]
while(decimal>0):
	if((decimal%16)<10):
		hex=decimal%16
		list.append(hex)
		decimal=decimal/16
	
	else:
		hex=chr((decimal%16)+55)
		list.append(hex)
		decimal=decimal/16
	
list.reverse()
print "the equivalent hex number is:    "

print ''.join(map(str, list))
'''for x in list:
	print x,'''