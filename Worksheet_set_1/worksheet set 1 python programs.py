#!/usr/bin/env python
# coding: utf-8

# In[64]:


# Write a python program to find the factorial of a number.

x = int(input('Enter a number: '))
if x < 0:
    print('Factorial is 0')
elif x==0 or x==1:
    print('Factorial is 1')
else :
    n = x
    factorial = 1
    while x > 1:
        factorial *= x 
        x-=1
    print('Factorial of', n ,'is: ',factorial)


# In[17]:


# Write a python program to find whether a number is prime or composite.

x = int(input('Enter a number: '))
if x>1:
    for i in range(2,x):
        if x%i == 0:
            print('Number is composite')
            break
        else:
            print('Number is prime')
elif x == 0 or x == 1 or x<0:
    print('Number is neither composite nor prime')


# In[27]:


# Write a python program to check whether a given string is palindrome or not.

word = list(input('Enter word: '))
reverse = word[::-1]
if word==reverse:
    print('Word is palindrome')
else:
    print('Word is not a palindrome')


# In[48]:


# Write a Python program to get the third side of right-angled triangle from two given sides.

a = int(input('enter length of perpendicualr of right angled triangle: '))
b = int(input('enter length of base of right angled triangle: '))
h = ((a)**2 + (b)**2)**(1/2)
print('Third side of triangle is',h)


# In[59]:


# Write a python program to print the frequency of each of the characters present in a given string

string = input('enter string: ')
freq_dict = {}
  
for i in string:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
print ("Count of all characters in GeeksforGeeks is :\n "+  str(freq_dict))

