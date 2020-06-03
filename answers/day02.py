#!/usr/bin/python
# Author:	@BlankGodd

def termino(x):
	count, i = 0, 0
	while i < len(x):
		cond = False
		if x[i] == '(':
			try:
				if x[i+1] == ')':
					cond = True
			except:
				pass
			else:
				pass
		else:	# val == ")"
			if i == 0:
				pass
			else:
				if x[i-1] == '(':
					cond = True
		if cond == False:
			count += 1
		i += 1
	return count


