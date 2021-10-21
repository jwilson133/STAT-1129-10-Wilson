#!/usr/bin/env python
# coding: utf-8

# In[90]:


#Question #1
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([1, 2, 3, 4])
y2 = np.array([5, 6, 7, 8])
y3 = np.array([9, 10, 11, 12])

plt.plot(y1, linewidth = '1')
plt.plot(y2, linewidth = '1')
plt.plot(y3, linewidth = '1')

plt.xlabel("X Label")
plt.ylabel('Y Label')

plt.show()


# In[96]:


#Question #2
data = np.random.normal(0,.2,800)

plt.hist(data, bins = 20)
plt.show()


# In[91]:


#Question #3
mydic = {"Apples":45, "Bananas":25, "Cherries":15, "Dates":20}

fruits = []
nums = []

for i in mydic:
    fruits.append(i)
    nums.append(mydic[i])
    
print(fruits)
print(nums)

plt.pie(nums, labels = fruits, explode = (.1,.1,.1,.1))
plt.show()
plt.bar(fruits, nums)
plt.show()


# In[88]:


#Question #4
marks_range = [10,20,30,40,50,60,70,80,90,100]

math_marks = [88,92,80,89,90,80,60,88,80,84]
science_marks = [75,59,69,48,65,56,32,45,20,30]

plt.scatter(marks_range, math_marks, color = 'r')
plt.scatter(marks_range, science_marks, color = 'g')
plt.legend(['Math Marks','Science Marks'])

plt.xlabel('Marks Region')
plt.ylabel('Marks Scored')
plt.title('Scatter Plot')

plt.show()


# In[134]:


#Questions #5
x = np.array([0,1,2,2,3,4,5,6])
y = np.array([5,3,7,8,1,2,6,2])

plt.subplot(1, 4, 1)
plt.scatter(x,y)
plt.title('Scatter Plot')

y = np.array([1,8,5,6])
y2 = np.array([5,6,2,9])

plt.subplot(1, 4, 2)
plt.plot(y)
plt.plot(y1)
plt.title('Multiple Line')

plt.subplot(1, 4, 3)
nums = np.array([5,6,2,9])
names  = np.array(['A','B','C','D'])
plt.bar(names, nums)
plt.title('Bar Graph')

data = np.random.normal(0,2,5000)
plt.subplot(1, 4, 4)
plt.hist(data, bins = 100)
plt.title('Histogram')

plt.show()


# In[ ]:




