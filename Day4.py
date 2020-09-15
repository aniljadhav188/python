#!/usr/bin/env python
# coding: utf-8

# # day 4 :Assignment

# In[2]:


lst=range(1042000,702648265)
add=0
count=0
x=0
y=0
while lst[x]!=lst[-1]:
      num=n=lst[x]
      count=0
      while n!=0:
          n=n//10
          count+=1
         
      while num>0:    
          y= num % 10
          add=add+pow(y,count)
          num=num//10
     # print(lst[x])
      if add==lst[x]:
        print("The first armstrong number",add)
        break
      x+=1 
      add=0


# In[ ]:




