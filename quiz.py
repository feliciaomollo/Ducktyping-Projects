name = input("Enter your name: ")
age = int(input("Enter your age: "))

future_age = age + 10

print (f"Hello {name}, your future age is {future_age} years old")

#Write a Python program that asks the user for their birth year and calculates their age.
    
dob = int (input ("Enter your birth year: "))
age = int (input("Enter your age: "))

current_age = (dob + age)

print (f"You are {current_age} years old")

from datetime import date

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Get the current year
current_year = date.today().year

# Calculate age
age = current_year - birth_year

# Print the result
print(f"You are {age} years old.")

