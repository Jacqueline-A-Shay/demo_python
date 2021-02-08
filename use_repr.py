# add 'dunder' and repr to class to be more Pythonic
# provide string representation of the object (created by using this class)
# for the consumer of the class

# __repr__ > more unambiguous
# __str__ > more readable for consumer

class first_car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        # return a PEP8
        return ('''{self.__class__.__name__}: {self.make}, {self.model}, {self.year}'''
		.format(self=self))
