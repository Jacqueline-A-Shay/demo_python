# define a new class
class titan:
	# initializer is called whenever a new object (aka variable, like eren shown below) 
	# is created
	# in this particular class, there are 2 instance attributes, unique to each new object
	# the 2 are: name and power

	# self is a constant, represent current object itself when this class being instantiate
	# Instantiating a class is creating a copy of the class 
	# which inherits all class variables and methods.
	def __init__ (self, name, power):
		
		self.name = name
		self.power = power
		print('{} is the {} titan'.format(self.name, self.power))

# calling the class as if we are calling a function
# the titan objects have unique name and power value
eren = titan('Eren', 'founder')
# we can modify an instance attributes like this
eren.power = 'a mixture of many titans...'
print(eren.power)


