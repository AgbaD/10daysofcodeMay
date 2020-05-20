#!/usr/bin/python
# Author:	@BlankGodd


# Task 1
def selection(seq):
	"""Selection sort implementation"""
	# [5,3,6,1,8,7,2]
	length = len(seq)
	for i in range(length):
		small = i
		for j in range(i+1, length):
			if seq[j] < seq[small]:
				small = j
		seq[i],seq[small] = seq[small],seq[i]


#######################################################


# Task 2
def short_sub(a,b):
	"""A function that returns the shortest possible sub string 
	containing all characters in the given set b"""
	for val in b:
		assert val in a
	x = []
	# structure, {t,u}
	y = {}
	ind = 0
	for val in a:
		if val in b:
			y[ind] = val
		ind += 1
	j = [i for i in y.keys()]
	start = min(j)
	maxi = max(j)
	add_word(y, start, maxi, a, b, x, j)
	length = len(x[0])
	wordd = x[0]
	for word in x:
		if len(word) < length:
			length = len(word)
			wordd = word
	return word

def add_word(y, start, maxi, a, b, x, j):
	stop = check(y, start, b, maxi)
	if stop:
		word = ''
		for i in range(start, stop+1):
			word += a[i]
		x.append(word)
		if start <= maxi:
			start += 1
			add_word(y, start, maxi, a, b, x, j)
	else:
		pass


def check(y, start, b, maxi):
	c = []
	while True:
		try:
			if y[start] in c:
				pass
			else:
				c.append(y[start])
		except:
			pass
		if set(c) == b:
			return start
		start += 1
		if start > maxi:
			break
	return False




if __name__ == "__main__":
	s = [3,2,1,4]
	selection(s)
	print(s)

	print(short_sub('structure', {'t','u'}))
	print(short_sub('figehaeci', {'i','e','a'}))
	print(short_sub('wednesday', {'d','e','f'}))

