#!/usr/bin/env python
# coding: utf-8

# ### Remove duplicates from an array in place?

# In[1]:


def remove(array):
    final_array = []
    for n in array:
        if n not in final_array:
            final_array.append(n)
            
    return final_array        



lists = [2,3,4,55,6,7,2,3,4,5,2,3]

n = remove(lists)

print(n)


# ### Find the largest and smallest number in an unsorted integer array?

# In[13]:


def largest_smallest_number(array,types):
    max_and_min_number  = array[0] 
    if types == "small":
        for n in array:
            if n < max_and_min_number:
                max_and_min_number = n
        print(max_and_min_number)        
    elif types == "larg":
        for n in array:
            if n > max_and_min_number:
                max_and_min_number = n
        print(max_and_min_number)        
    else:
        print("Please enter the correct type ")
        
        
lists = [2,3,45,6,78,9,1,55,33,4466]

largest_smallest_number(lists,"small")


# ### How to Print duplicate characters from String?

# In[16]:


chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking this string to see how many times each character appears"
for char in chars:
    
    count = check_string.count(char)
    if count > 1:
        print(char, count)


# ### How to check if a String contains only digits?

# In[18]:


s = '112344'
s.isdigit()


# ### Implement Binary search using python language?

# In[20]:


def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1   
            else:
                first = mid + 1
    return found
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


# ### Find the Factorial of the number?

# In[32]:


number = input("Enter the number to convert factorial  ")
fact = 1 
if number < "0" :
    print("Enter the positive values ")
elif number == "0":
    print("The factorial of 0 is equal to 1 ")
else:
    for i in range(1,int(number)+1):
        fact = fact*i
    print(f"Factorial of {number}  is  {fact}")    


# ### How to check if a given year is a leap year?

# In[35]:


year = 2021

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

