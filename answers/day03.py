#!/usr/bin/python
# Author:	@BlankGodd

dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def itos(x):
	"""Converts intergers to strings"""
	if type(x) != int:
		raise ValueError("Input value not an integer!")
	return '{}'.format(x)

def stoi(x):
	"""Converts strings to integers"""
	if type(x) != str:
		raise ValueError("Input value not a string")
	try:
		ans = 0
		for d in x:
			ans = 10 * ans + dic[d]
		return ans
	except:
		raise ValueError("Input value not a string")

def stof(x):
	"""Converts strings to float"""
	if type(x) != str:
		raise ValueError("Input value not a string")
	try:
		ans = 0
		d = 1
		f = [i for i in x.split(".")]
		for b in f[0]:
			ans = 10 * ans + dic[b]
		for a in f[1]:
			d = d/10
			ans = d * dic[a] + ans
		return ans
	except:
		raise ValueError("Input value not a string")


def ftos(x):
	"""Converts floats to strings"""
	a = '{}'.format(x)
	try:
		b = [i for i in a.split(".")]
	except:
		raise ValueError("Input value not a float!")
	try:
		x * x
	except:
		raise ValueError("Input value not a float")
	return a


