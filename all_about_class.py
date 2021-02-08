# define a new class
class titan:
	# create a class attribute
	# if not purposely changed, this will be the default
	source = 'Japanese anime'
	
	# initializer is called whenever a new object (aka variable, like eren shown below) 
	# is created
	# in this particular class, there are 2 instance attributes, unique to each new object
	# the 2 are: name and power

	# self is a constant, represent current object itself when this class being instantiate
	# Instantiating a class is creating a copy of the class 
	# which inherits all class variables and methods.
	
	# take the name and power input and assign to the newly created object, aka, self
	def __init__ (self, name, power):
		
		self.name = name
		self.power = power
		
	def output(self):
		print('{} is the {} titan'.format(self.name, self.power))

	def output_add_lname(self):
		last_name = input("Do you remember {}'s last name?".format(self.name))
		full_name = self.name+' '+last_name
		return full_name

	
# calling the class as if we are calling a function
# the titan objects have unique name and power value
eren = titan('Eren', 'founder')
eren.output()
print('...')
print(f'the full name of {eren.name} is about to show...',eren.output_add_lname())

# we can modify an instance attributes like this
eren.power = 'a mixture of many titans...'
print('something about {} is his power is basically {}'.format(eren.name, eren.power))
print('{} is a character from a {}, Attack on Titan'.format(eren.name,eren.source))


