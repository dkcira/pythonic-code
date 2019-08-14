# PEP 8

# Code Layout

# blank lines break code into pieces,
# like paragraph break text into ideas

# top level: 2 blank lines each. class methods, single blank lines
# single blank lines within functions too


class MyFirstClass():
	def first_method(self):
		pass

	def second_method(self):
		pass


class MySecondClass():
	pass


def top_level_function():
	pass


def calculate_variance(number_list):
	sum_list = 0
	for number in number_list:
		sum_list = sum_list + number
	mean = sum_list / len(number_list)

	sum_squares = 0
	for number in number_list:
		sum_squares = sum_squres + number**2
	mean_squares = sum_squares / len(number_list)

	return mean_squares - mean**2

# maximum line length: 79 characters
# use implied continuation within parameters, brackets, curly braces


def function(arg_one, arg_two,
	         arg_threww, arg_four):
	return arg_one

# no parenthesis or brackets? use backslash

from mypgk import example1, \
	example2, example3

# easier to read if you break before the operator

total = (first_variable
		+ second_variable
		- third_variable)









