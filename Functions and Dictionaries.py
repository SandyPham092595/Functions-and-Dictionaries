# Functions and Dictionaries

# 1. Dictionaries:
# Create a dictionary to store information about three friends, such as their name, favorite hobby, and favorite food. Print each person's information in a clean format (Chapter 6).
friend_dictionary = {
    'David Cliff': {'hobby': 'surf', 'food': 'barbeque ribs'},
    'Harriet Waller': {'hobby': 'write', 'food': 'strawberry shortcake'},
    'Tamara Webb': {'hobby': 'cook', 'food': 'ceaser salad'}
}
# lower case all hobby and food values
for friend in friend_dictionary.values():
    friend['hobby'] = friend['hobby'].lower()
    friend['food'] = friend['food'].lower()

print("David Cliff likes to " + friend_dictionary['David Cliff']['hobby'] + " and eating " + friend_dictionary['David Cliff']['food'] + ".")
print("Harriet Waller likes to " + friend_dictionary['Harriet Waller']['hobby'] + " and eating " + friend_dictionary['Harriet Waller']['food'] + ".")
print("Tamara Webb likes to " + friend_dictionary['Tamara Webb']['hobby'] + " and eating " + friend_dictionary['Tamara Webb']['food'] + ".")

# 2. User Input:
# Write a program that asks for the user's age and prints a message based on whether they are a child, teenager, or adult (Chapter 7).
age = input("How old are you? ")
age = int(age)
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 3. Functions:
# Create a function that takes two numbers as arguments and returns their product. Write another function that takes a list of numbers and returns the sum of all the numbers in the list (Chapter 8).

# Product function.
print("Enter two numbers to multiply: " )
first_number = input("First number: ")
first_number = int(first_number)
second_number = input("Second number: ")
second_number = int(second_number)
def product(first_number, second_number):
    return first_number * second_number
print("The product of " + str(first_number) + " and " + str(second_number) + " is " + str(product(first_number, second_number)) + ".")

# Sum function.
print("Enter a list of numbers to add together: ")
number_list = []
while True:
    number = input("Enter a number or press enter to finish: ")
    if number == "":
        break
    number = int(number)
    number_list.append(number)
def sum_list(number_list):
    return sum(number_list)
print("The sum of the numbers in the list is " + str(sum_list(number_list)) + ".")

# https://github.com/SandyPham092595/Functions-and-Dictionaries.git