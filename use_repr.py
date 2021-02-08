# add 'dunder' and repr to class to have Pythonically print out
# the result after using class to create object
# instead of only getting memory address of the object
# or a string containing the class name and id of the object

class first_car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def __repr__(self):
	# return a PEP8
		return ('{self.__class__.__name__}(
			{self.make}, {self.model},{self.year})'.format(self=self)


