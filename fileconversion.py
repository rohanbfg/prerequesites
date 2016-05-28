from sys import argv

script,from_file = argv
data=open(from_file)
j=4
txt=open('C:\Users\Rohan\prerequesites\converted_data.txt','w')
while(1):
	d=data.read(5)
	txt.write(d)
	txt.write("\n")
	data.seek(j+2)
	d=data.read(1)
	txt.write(d)
	txt.write("\n")
	data.seek(j+4)
	j=j+8
data.close()
