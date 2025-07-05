# Program specification
"""
Write a program that examines three variables—
x, y, and z—and prints the largest odd number among them. If none
of them are odd, it should print the smallest value of the three.
"""

numbers = []
for i in range(3):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("You entered:", numbers)

odd = []
even = []
for number in numbers:
    if number % 2 != 0:
        odd.append(number)
    else:
        even.append(number)

if len(odd) != 0:
    print("The largest odd number is", max(odd))
else:
    print("The smallest value is", min(numbers))