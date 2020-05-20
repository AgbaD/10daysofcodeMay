python | Intermediate | 16

BUBBLE SORT
 

Write a function bubble_sort  that takes in an array of integers and sorts the elements of the array  using bubble sort algorithm and RETURNS number of swaps required to sort the array completely

 

 

Working of bubble sort
Given an unsorted array e.g

[3,2,1,4]

 

The first iteration we compare 3 and 2 since 3>2 we swap 3 and 2

 

The array becomes

[2,3,1,4]

 

Next we compare 3 and 1

3>1 so we swap them

 

[2,1,3,4]

 

Next we compare 3 and 4

3<=4 so no swap

 

[2,1,3,4]

 

 

We repeat the process from the beginning until we get the final result

 

[1,2,3,4]

Try reading more on bubble_sort so you fully understand the problem.

Try to optimize you code to do as few iterations as possible.

SAMPLE CASES
 

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

c=[9, 10, 6, 2, 3, 5, 4, 8, 7, 1]

 

print(bubble_sort(a)) #prints 0

print(a) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

print(bubble_sort(b)) #prints 45

print(b) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

print(bubble_sort(c)) #prints 29

print(c) #prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

NOTE
•Only AssertionErrors  should be RAISED if need be

•NO INBUILT MODULES SHOULD BE USED

•DON'T USE sort() or sorted() FUNCTION.(It may result in an automatic 1)

 

Goodluck