# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
l1=[10,23,45,32,67]
l2=[11,14,26,48,29]
l3=[]
l3.append([i for i in l1 if i%2!=0])
l3.append([i for i in l2 if i%2==0])
print(l1,l2,l3)