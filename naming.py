# PEP 8

# Naming Conventions

# functions, lowercase word or words  + underscores
def my_function():
	pass

# variables, same rules, but you can use single letters
x = 2
my_variable = 'two'

# constants, all capital letters + underscores
GRAVITY_ACCELERATION = 9.8

# classes. Start each word with capital letter, no underscores.
# class methods: same as functions
class CoolCat():
	def meow():
		pass

# modules: lowercase + underscores
my_module.py

# packages: lowercase, no underscores
mypackage



# single letter variable names ok for math functions, bot not for names
x = 'John Smith' # no!
y, z = x.split()
# instead
name = 'John Smith'
first_name, last_name = name.split()

# shorten function names?
def db(x): # no
	return x * 2

def multiply_by_2(x): # yes
	return x * 2






