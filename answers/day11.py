#!/usr/bin/python
# Author:	@BlankGodd

def resolve(dic,lst):
	# d = {'a':'b','b':'c','p':'q','q':'p','z':'z'}
	# l = [a,b,p,q,z]
	res = []
	a = [i for i in dic.keys()]
	for val in lst:
		x = dic[val]
		if x in a:
			y = x
			while y in a:
				y = dic[y]
				if y not in a:
					res.append(y)
					break
				elif y == val:
					res.append(val)
					break
				elif y == x:
					res.append(x)
					break
				else:
					pass
		else:
			res.append(x)
	return res


