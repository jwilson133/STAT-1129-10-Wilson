#!/usr/bin/env python
# coding: utf-8

# In[40]:


#Question #1
import numpy as np

numbers = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
numbers2 = numbers * 2

print(numbers2.ndim)
print(numbers2.shape)


# In[41]:


#Question #2
for row in numbers:
    for column in row:
        print(column, end=' ')
    print()
    
print()
    
for row in numbers:
    for column in row:
        print(column, end=' ')


# In[42]:


#Question #3
import matplotlib.pyplot as plt

xpoints = np.array([1,2,3,4,5,6])
ypoints = np.array([5,6,7,8,9,10])

plt.plot(xpoints, ypoints)
plt.show()


# In[43]:


#Question #4
xpoints = np.array([3,6,9,12])
ypoints = np.array([2,8,1,10])

plt.plot(xpoints, ypoints, marker = 'D')
plt.show()


# In[44]:


#Question #5
xpoints = np.array([0,1,2,3,4,5])
ypoints = np.array([2,4,6,14,10,12])

plt.plot(xpoints, ypoints, 'D--r', ms = 10, mfc = 'g', mec = 'g')
plt.show()


# In[ ]:




