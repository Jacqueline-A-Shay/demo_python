types_of_people = 10
x = f"there are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"

jaja = 123
jaja_max = "calling out jaja {}"
print(jaja_max.format(jaja))

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
print(f"hilarious meaning {hilarious}")

joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation)

print(joke_evaluation.format(hilarious))
print(f"joke_evaluation {x}")

w = "this is the left side of ..."
e = "a string with a right side"
z = w+e
print(w+e)
print(z)
