class titan:
	def __init__ (self, name, power):
		self.name = name
		self.power = power
		print('{} is the {} titan'.format(self.name, self.power))


e = titan('Eren', 'founder')
e.power = 'a mixture of many titans...'
print(e.power)
#print('{} is the {} titan'.format(devil.name, devil.power))
