#!/usr/bin/python
# Author:	@BlankGodd

# Task 1

def insertion(seq):
	# [5,3,6,1,8,7,2]
	b = 1
	while b < len(seq):
		a = b
		while a > 0: 
			if seq[a] < seq[a-1]:
				seq[a-1], seq[a] = seq[a], seq[a-1]
			else:
				break
			a -= 1 
		b += 1

# Task 2
def biggie(seq,a):
    x,y = a+1,a-1
    val = seq[a]
    length = len(seq)
    tries = 0
    while tries < length:
        if y == -1:
            y = a
        if x == length:
            x = a
        try:
            if seq[x] > val:
                return x
            if seq[y] > val:
                return y
        except:
            pass
        x += 1
        y -= 1
        tries += 1 
    raise AssertionError('No nearest larger integer')


if __name__ == '__main__':
    a = 'australia'
    a = [i for i in a]
    b = [5,3,6,1,8,7,2]
    insertion(a)
    insertion(b)
    print(a)
    print(b)
    b = [5,3,6,1,8,7,2]
    c = [4, 1, 3, 5, 6]
    print(biggie(c,0))
    print(biggie(b,4))
