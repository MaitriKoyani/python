# Exercise 9: Check Palindrome Number
n=(input('Enter number:'))
if n==n[::-1]:
    print('it\'s palindrome')
else:
    print('it\'s not palindrome')