# Exercise 3: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
def calculate(a,b):
    return (a+b),(a-b)
print("Calculation: ",calculate(40,30))