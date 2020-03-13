#!/usr/bin/env python
# coding: utf-8

# ### Write and then read a file in CSV format?

# In[1]:


import csv 


# In[9]:


# my data rows as dictionary objects  
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},  
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},  
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},  
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},  
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},  
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]  
# field names  
fields = ['name', 'branch', 'year', 'cgpa'] 

  
# name of csv file 
filename = "university_records.csv"
  
# writing to csv file 
with open(filename, 'w',encoding = 'utf-8') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
    # writing headers (field names) 
    writer.writeheader()   
    # writing data rows 
    writer.writerows(mydict) 


# In[10]:


with open(filename, 'r',encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))


# ###  Difference between Def and lambda?
# 

# In[27]:


def add(x,y):
    return x+y

adding = lambda x,y : x+y

print("function",add(4,5))
print("lambda function", adding(4,5))


# In[38]:


def find_out(value):
    if (value % 2) == 0 :
        return "even"
    else:
        return "odd"


even_odd = lambda x: "Even" if(x % 2)==0 else "Odd"   

values = 5    
n = find_out(values)
print(f"from function  value is {values} = {n}")
print(f"from lambda function  value is {values} = {n}")


# ###  Lamda map and filter function?

# In[48]:


lists = [0,2,3,4,5,6,78,88,22,33]

n = list(map(lambda x: x*3,lists))

m = list(filter(lambda x: (x%2==0),lists))

print(f"lambda map function  {n}")
print(f"lambda filter function  {m}")


# ### Write a function to compute Nth Fibonacci number

# In[4]:


def fibonacci(n):
    array = []
    a = 0 
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            array.append(b)
    return array




n = fibonacci(16)
print(n)


# ### Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 ﬁnd which number is not present in the second array by creating a function  and passing array as arguments

# In[93]:


# Function for finding elements which  
# are there in a[] but not in b[]. 
def findMissing(a, b, n, m): 
  
    for i in range(n): 
        for j in range(m): 
            if (a[i] == b[j]): 
                break
  
        if (j == m - 1): 
            print(a[i], end = " ") 
  

      
a = [ 1, 2, 6, 3, 4, 5 ] 
b = [ 2, 4, 3, 1, 0 ] 
n = len(a) 
m = len(b) 
findMissing(a, b, n, m) 


# In[ ]:




