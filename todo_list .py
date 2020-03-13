#!/usr/bin/env python
# coding: utf-8

# ### Create user name list 

# In[1]:




lists = [] 

n = 0
print("-1 to exit the program")
while(True):
    
    if (n == 0 ):
        
        name = input("Enter the name ")
        lists.append(name)
        if name == "-1":
            lists.remove("-1")
            n = -1
    else:
        break
    
    
    
   


# ### Find the name in list
# 

# In[6]:


findName = input("Enter find name ")

if findName in lists:
    print("found Name in list")
else:
    print("Not found in list")


# In[ ]:




