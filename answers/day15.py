#!/usr/bin/python
# Author:	@BlankGodd

#################################################

# Task 1
def adder(ary):
	# ['2/21','1/9','8/63']
	z = [i.split("/") for i in ary]
	deno = []	# denominator
	for x in range(len(z)):
		deno.append(int(z[x][1]))
	g = lcm(deno[0], deno[1])
	if len(deno) > 2:
		i = 2
		while i < len(deno):
			g = lcm(g, deno[i])
			i += 1
	num = []
	for x in range(len(z)):
		num.append(int(z[x][0]))
	x = 0
	for i in range(len(z)):
		x += (g/deno[i])*num[i]
	a = [2,3,5,7]
	for i in range(4):
		for val in a:
			if x%val == 0 and g%val == 0:
				x /= val
				g /= val
	return '{0}/{1}'.format(int(x),int(g))

def gcd(a,b):
	if a == 0:
		return b
	return gcd(b%a, a)

def lcm(a,b):
	return (a*b)/gcd(a,b)

###################################################

# Task 2
def swap(a,b):
	a,b = b,a
	return a,b



if __name__ == "__main__":
	s = ['2/21','1/9','8/63']
	v = ['1/2','1/3','1/6']
	print(adder(s))
	print(adder(v))

	print(swap(8,9))


