# do a format with extra variables as in f"{x} {y}"
# y = input("Name? ")

# prompt user input their age height and weight
# making sure the data type is correct, since input() will return string
# making sure the unit is right

def ask_user_age_height_weight():
	# prompt user location and unit preference
	# so we could decide following unit conversion method
	geo_of_user = input("Will you share where were you from?\nenter: imperial or metrics ")
	# prompting the user info
	age = int(input("How old are you? "))
	height = input("How tall are you? ")
	weight = float(input("How much do you weigh? "))
	# if user prefers imperial, then we will explicitly ask them to provide ft and inch
	# we currently do not want to further complicate the program
	if geo_of_user == 'imperial':
		if "'" 	not in height:

			get_ft = input("Enter ft please: ")
			get_in = input("Enter inch please: ")
			print(f'So you are {age} years old,\nyou are {get_ft}ft and {get_in}in tall\nand you weigh {weight}lb')
		else:
			print(f'so you are {age} years old,\n{height} tall and weigh {weight}') 
	elif geo_of_user == 'metrics': #elif = else if
	# if user prefers metrics, we can proceed with this process
		print(f'so you are {age} years old,  {height}cm tall, and you weigh {weight}kg')	
	
	else:
		print('please start over')	

ask_user_age_height_weight()
#print(f'So you are {age} years old, and you are {round(height/30.48)}ft and {round((height%30.48)/2.54)}in tall and you weigh {round(weight*2.205,2)}lb')
