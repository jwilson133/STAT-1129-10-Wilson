#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Question 0

marks = {'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}

#Question 1
print('Question 1')

for i in marks:
    print(i, marks[i])
    
#Question 2
print()
print('Question 2')

total = 0
count = 0
for i in marks:
    total += marks[i]
    count += 1
mean = total/count
print('Mean:', mean)

highest = 0
lowest = 100
for i in marks:
    if marks[i] >= highest:
        highest = marks[i]
    if marks[i] <= lowest:
        lowest = marks[i]
print('Maximal Grade:', highest)
print('Minimal Grade:', lowest)
    

#Question 3
print()
print('Question 3')

for i in marks:
    if 'J' in i or 'j' in i:
        break
    print(i)

#Question 4
print()
print('Question 4')

for i in marks:
    if 'J' in i or 'j' in i:
        continue
    print(i)

#Question 5
print()
print('Question 5')

def grade_finder(student, marks):
    for i in marks:
        if i == student:
            return marks[i]
            break
    else: print('Cannot find this students name')
        
            
print(grade_finder('Jules', marks)) 

#Question 6
print()
print('Question 6')

def power_two(num):
    n = 0
    while n < num:
        print('n =', n,'n^2 =', n**2)
        n += 1
    print(n, 'is greater than or equal to', num)
        
power_two(8)

#Question 7
print()
print('Question 7')

def add_up(num):
    n = 1
    total = 0
    while n <= num:
        total += n
        n += 1
    print('Total =', total)

add_up(8)

#Question 8
print()
print('Question 8')


#Question 9
print()
print('Question 9')

def add_up(num):
    n = 1
    total = 0
    for n in range(num+1):
        total += n
        print('Total at', n,'=',total)
        n += 1
    print('Total =', total)

add_up(8)

#Question 10
print()
print('Question 10')

def minimal(v1, v2, v3, v4):
    minimum = v1
    if minimum > v2:
        minimum = v2
    if minimum > v3:
        minimum = v3
    if minimum > v4:
        minimum = v4
    return minimum 
print(minimal(6,2,5,3))


# In[3]:





# In[ ]:





# In[ ]:




