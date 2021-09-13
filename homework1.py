#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Problem #1
colors = ['Red', 'Blue', 'Green', 'Silver']
print(colors)


# In[4]:


# Problem #2
n = 30
m = 60
numbers = []
for i in range(100):
    numbers.append(n)
    n += 3
    if n > m:
        break
numbers_t = tuple(numbers)

print(type(numbers))
print(type(numbers_t))


# In[5]:


# Problem #3
three = []
n = 0
for i in range(6):
    three.append(n)
    n += 1
    
print(three)
three.remove(2)
print(three)
three.insert(2, 2.0)
print(three)

print('Length:', len(three),'Max:', max(three), 'Min:', min(three))


# In[3]:


# Problem #4
tenlist = []
n = 1
for i in range(10):
    tenlist.append(n)
    n += 1
    
print(tenlist)
total = sum(tenlist)
print('Sum:', total)


# In[ ]:




