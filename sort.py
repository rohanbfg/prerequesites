import random
import sys
import os

print"enter the names"
string_input=raw_input()#taking string as input
names=string_input.split()#split function splits the input string on spaces and assigns each string to the list
names.sort()#sorts the list


print names

