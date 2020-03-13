#!/usr/bin/env python
# coding: utf-8

# <h3>Q1 - Write a program that asks the user for a number n and prints the sum of the numbers 1 to n</h3>

# In[1]:


sum = 0
number = input("Enter number   ")

for i in range(1,int(number)):
    sum = sum + i
    print(sum)


# ### Q2-  Write a program that prints a multiplication table for numbers up to 12.

# In[2]:


table_number = input("Enter Table number  ")

for i in range(1,11):
    print(f"{table_number} * {i} = {int(table_number)* i} ")


# ### Q3- Write a function that returns the largest element in a list.

# In[3]:


def largest_number(array,length):
    max_number = array[0]
    
    for i in range(0,int(length)):
        if(array[i] > max_number):
            max_number = array[i]
    
    return max_number




length = input("Enter the length of list ")
lists = []
for i in range(1,int(length)+1):
    new_number = input("Enter new number")
    lists.append(new_number)

print(lists)
get_number = largest_number(lists,len(lists))
    
print("largest number in list  " , get_number)    


# ### Q4-  Write a function that computes the running total of a list.

# In[4]:


def sum_list(n):
    sum_values = 0; 
    for i in n:
        sum_values = sum_values + i 
    return sum_values


lists = [3,4,5,6,7,8]
sum_values = sum_list(lists)

print("Sum all values in list " , sum_values)


# ### Q5- Write a function that checks whether an element occurs in a list.

# In[3]:


def element_found_in_list(lis,values):
    rang = len(lis)
    for i in range(0,rang):
        if lis[i] == values:
            return "Found"
    
    

    
lists = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
n = element_found_in_list(lists,"mango")
print(n)

    
    


# ### Write a function that returns the elements on odd positions in a list.

# In[18]:


def funtion_lists(lis):
    length = len(lis)
    for i in range(0,length,2):
        print(lis[i])

lists = [1,2,3,4,5,6,7,8,9]
funtion_lists(lists)


# In[ ]:




