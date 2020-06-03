#!/usr/bin/python
# Author:	@BlankGodd

class Student:

	def __init__(self, age, weight, height):
		self.age = age
		self.weight = weight
		self.height = height
		

	def info(self):
		bmi = self.weight / (self.height**2)
		val = round(bmi, 2)
		return self.age, val


def average(lst):
	age = []
	weight = []
	height = []
	for val in lst:
		age.append(val.age)
		weight.append(val.weight)
		height.append(val.height)
	age_t = [(10+i) for i in age]
	avgage = (sum(age_t)/len(age_t))
	avg_age = round(avgage, 2)
	weight_t = []
	for val in weight:
		for i in range(10):
			val = (0.05 * val) + val
		weight_t.append(val)
	avgweight = (sum(weight_t)/len(weight_t))
	avg_weight = round(avgweight, 2)
	height_t = []
	for val in height:
		for i in range(10):
			val = (0.02 * val) + val
		height_t.append(val)
	avgheight = (sum(height_t)/len(height_t))
	avg_height = round(avgheight, 2)

	return avg_age, avg_weight, avg_height

	
