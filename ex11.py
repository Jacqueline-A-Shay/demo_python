# put an end = ' ' at the end of each print line
# this tells print to not end the line with a newline character and go to the next line
print("How old are you?", end = ' ')
# since the result yielded from the input() function will be string
# need to explicitly convert into integer 
# so I can do math with the result
age = int(input())
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"so, you're {age} old, {height} tall, and {weight} heavy.")

age2 = input("what's your age? ")
print(f'I\'ll make you younger by 10 yrs {int(age2)-10}\nand age-age2 = {age-int(age2)}')

