#!/usr/bin/python
# Author:	@BlankGodd

def bubble_sort(seq):
	"""Bubble sort implementation"""
	# seq = [4,8,6,3,7,2]
	count = 0
	length = len(seq)
	for i in range(length - 1):
		sorted = True
		for j in range(length - 1):
			if seq[j] > seq[j+1]:
				seq[j],seq[j+1] = seq[j+1],seq[j]
				count += 1
				sorted = False

		if sorted:
			break
	return count

if __name__ == "__main__":
	seq = [9,10,6,2,3,5,4,8,7,1]
	print(bubble_sort(seq))
	print(seq)


	