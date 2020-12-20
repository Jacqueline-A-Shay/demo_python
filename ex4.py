# assigning variables
# we are writing this program to automate the process of calculating carpool condition based on availability of car, drivers, and the amount of passengers waiting for carpool
# cars: int, tell us how many cars do we have today
cars = 100
space_in_a_car = 4
print(space_in_a_car)

drivers = 30
passengers = 90

cars_not_driven = cars  - drivers
cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car
average_passengers_in_a_car = passengers / cars_driven

# printing out the math/ results
print("""There are {} cars available.
There are only {} drivers available.
There will be {} empty cars today.
We can transport {} people today.
We have {} to carpool today.
We need to put about {} in each car.
""".format(cars, drivers, cars_not_driven, carpool_capacity, passengers, average_passengers_in_a_car))

testing_str_substraction = ['test','t'] - ['test']
print(testing_str_substraction) 
