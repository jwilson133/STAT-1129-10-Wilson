#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Question 1
n = 0
while( n < 10 ):
    if n == 5:
        break
    print(n)
    n += 1


# In[21]:


# Question 2
n = 0
while( n < 5 ):
    print(n)
    n += 1
    if n >= 5:
        print(n, 'is not less than 5')
        break


# In[22]:


# Question 3
fruits = ['banana', 'orange', 'blueberry', 'strawberry', 'apple', 'mango']
for i in range(len(fruits)):
    if fruits[i] == 'apple':
        print('apple is really a fruit?')
        break
    print('I like', fruits[i])


# In[23]:


# Question 4
total = 0
for i in range(1,31):
    total = total + i
print(total)


# In[24]:


# Question 5
weather = {'sunny' : 'play', 
           'rainy' : 'watch TV', 
           'cloudy' : 'walk'}
for i in weather:
    print('When', i, 'let us', weather[i])
    
weather['snow'] = 'ski'
print(weather)    


# In[25]:


# Question 6
weather = {'sunny' : 'play', 
           'rainy' : 'watch TV', 
           'cloudy' : 'walk'}
for i in weather:
    print('When ', end='')
    if i == 'sunny':
        print(i, 'let us', weather[i])
    if i == 'rainy':
        print(i, 'let us', weather[i])
    if i == 'cloudy':
        print(i, 'let us', weather[i])


# In[26]:


# Question 7
grades = {(90,100): 'A', 
          (80,90) : 'B',
          (70,80) : 'C',
          (60,70) : 'D',
          (0,60) : 'F'}

students = {'John' : 65,
            'Beth' : 73,
            'Carl' : 96,
            'Jess' : 81,
            'Ben' : 23,
            'Julia' : 90}

for i in students:
    for j in grades:
        top = j[1]
        bottom = j[0]
        if bottom <= students[i] < top:
            print(i, students[i], '=', grades[j])


# In[ ]:





# In[ ]:




