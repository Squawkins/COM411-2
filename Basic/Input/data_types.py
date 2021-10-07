print("What is your name human?")
name = input()


print ("\n \n How old are you?")
age = input()

print("\n \n How tall are you?(in M)")
height = float(input())

print("\n \n How much do you weigh?(in KG)")
weight = int(input())


bmi=float(weight) / float(height**2)


print(f"\n \n {name} you are {age} years old and have a BMI of {bmi}")







