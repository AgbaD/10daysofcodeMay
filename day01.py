#!/usr/bin/python
# Author:	@BlankGodd

def average(x):
	a = [int(i) for i in x.split(" ")]
	b = sum(a)
	return b/len(a)

x = '12 11 2 6 7 10'
print(average(x))