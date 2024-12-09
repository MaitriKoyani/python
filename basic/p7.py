# Exercise 7: Find the number of occurrences of a substring in a string
str=input('Enter string:')
l1=str.split(' ')
l2=[]
for i in l1:
    if l1.count(i)>1 and i not in l2:
        print(f'{i} found {l1.count(i)} times.')
        l2.append(i)