#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Generate the following pattern
  	*
   	*  *
	*  *  *
 	*  *  *  *
 	*  *  *  *  *


# In[1]:


rows=int(input("Enter number of rows"))
for i in range(0,rows):
    for j in range(0,i+1):
        print('*',end=" ")
        
    print("\r")


# In[ ]:


2. Display multiplication table of K. Take k value from user
 	Ex:      7 x 1 =7
    		7 x 2 = 14   .....


# In[2]:


n=int(input("Enter the n value"))
for i in range(1,11):
    print(n,'x',i,'=',n*i)


# In[ ]:


#. Roots of quadratic equation
  	Take the coefficients a,b,c from the user


# In[6]:


import cmath
a=int(input("enter the a value"))
b=int(input("enter the b value"))
c=int(input("enter the c value"))
d=(b**2)-(4*a*c)
root1=((-b + cmath.sqrt(d))/2*a)
root2=((-b - cmath.sqrt(d))/2*a)
print("the roots are",root1,root2)


# In[ ]:


5. Generate first N number of Fibonacci numbers. Take N value from the user


# In[8]:


n=int(input("Enter the value n"))
f1=0
f2=1
for x in range(0,n):
    print(f2,end=" ")
    next=f1+f2
    f1=f2
    f2=next


# In[ ]:




