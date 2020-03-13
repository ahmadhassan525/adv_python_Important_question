#!/usr/bin/env python
# coding: utf-8

# ### Method Overloading 

# In[ ]:


# same function name but different parameter is call method overloading 


class conceptOverloading:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    
    def sum(self,a=None,b=None,c=None):
        s = 0 
        if a!= None and b!= None and c!= None:
            s = a+b+c
        elif a!=None and b !=None:
            s = a + b
        else:
            s = a 
        
        return s
    
    

s1 = conceptOverloading(3,4)


print("Three parameter",s1.sum(2,3,4)) 
print("Two parameter",s1.sum(2,4)) 
print("One parameter",s1.sum(4)) 
        
        


# ###  Method Overriding

# In[ ]:


class A_parent:
    def phone():
        print("Father Phone")
        
class B_child(A_parent):
    
    def phone():
        print("Child Phone")




s1 = B_child

s1.phone()


# ### Inheritance

# In[4]:


class Student:
    def feature1(self):
        print("feature 1 is working in class student ")
    def feature2(self):
        print("feature 2 is working in class student ")    
    
class Transport():
    def feature3(self):
        print("feature 3 is working in class Transport ")
    def feature4(self):
        print("feature 4 is working in class Transport ")
        
        
class Library(Transport,Student):
    def feature5(self):
        print("feature 5 is working in class Library ")

        
s = Library()
s.feature1()
s.feature2()
s.feature3()
s.feature4()
s.feature5()


# ### Constructor in Inheritance

# In[10]:


class Student:
    def __init__(self):
        print(" Constructor Student")
    def feature1(self):
        print("feature 1 is working in class student ")
    def feature2(self):
        print("feature 2 is working in class student ")    
    
class Transport():
    def __init__(self):
        print(" Constructor Transport")
    def feature3(self):
        print("feature 3 is working in class Transport ")
    def feature4(self):
        print("feature 4 is working in class Transport ")
        
        
class Library(Student,Transport):
    def __init__(self):
        super().__init__()
        print(" Constructor Library")
        
    def feature5(self):
        print("feature 5 is working in class Library ")
        
        
c  = Library()

        
        
        
        


# ### Encapsulation

# In[20]:


class Student:
    __name = "" 
    __age  = 0
    __program = ""
    
    def __init__(self,name= " demo",age = 0 ,program = "BS"):
        self.__name = name
        self.__age = age 
        self.__program
    
    def setName(self , name):
        self.__name = name
     
    
    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.__age = age
    
    def getAge(self):
        return self.__age
    
    def setProgram(self,program):
        self.__program = program
        
    def getProgram(self):
        return self.__program
    
    

    
s = Student()  

s.setName("Ahmed")
print(s.getName())
s.setAge(22)
print(s.getAge())
s.setProgram("BSCS")
print(s.getProgram())
    
    
    


# ### Abstract Class and Abstract Method

# In[12]:


from abc import ABC ,abstractmethod


class Computer(ABC):
    @abstractmethod
    def keyborad(self):
        pass
    def Mouse(self):
        pass

    
class computer_parts(Computer):
    
    def keyborad(self):
        print("Sumsung Keybord")
    
    def accessoires(self):
        print("Addition parts")
        

class customer():
    
    def product(self,com):
        print("product adding ")
        com.keyborad()
        

        
c = computer_parts()
c.accessoires()
c.keyborad()

c1 = customer()
c1.product(c)
    





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


from itertools import combinations
lst=[]
x = int(input())
y = int(input())
z = int(input())
n = int(input())

lst=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]

finallst=[]
for items in combinations(lst,3):
    for nums in items:
        
        x=sum(nums)
        if x!=n and nums not in finallst:
            finallst.append(nums)

f_finallst= sorted(finallst, key=str) #converted to string to get lexicographic order


# In[1]:


12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print



[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]


# In[ ]:


list = []
n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 3:
        eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("list." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print(lists)
    else:
        eval("list." + a[0] + "()")


# In[ ]:


n = int(input())
integer_list = map(int, input().split())

integer_list


# In[ ]:




