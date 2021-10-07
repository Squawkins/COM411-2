first_number = input(f"Please enter a whole number.")
second_number = input(f"\n\nPleas enter a second whole number.")
third_number = input(f"\n\nPlease enter a third whole number.")


even_number = 0
odd_number = 0

if int(first_number) % 2 != 0:
    odd_number += 1
else:
    even_number += 1

if int(second_number) % 2 != 0:
    odd_number += 1
else:
    even_number +=1

if int(third_number) % 2 != 0:
    odd_number += 1
else:
    even_number += 1

print(f"\n \nThere was {even_number} even and {odd_number} odd numbers.")