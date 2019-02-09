#!/usr/bin/env python
# coding: utf-8

# # Some basic python code

# In[1]:


# this is commented out


# In[ ]:


# Some keyboard shortcuts:
# Insert a cell above the selected one: Esc, a
# Insert a cell below the selected one: Esc, b

# For complete list, see Help -> Keyboard shortcuts


# In[1]:


# load all functions in numpy
# names of the functions will then be np.function 
import numpy as np

# load all functions in numpy, without requiring np. in the names:
# (but be careful with this, since several packages can have functions with the same names)
#from numpy import *

# load a particular function in numpy:
#from numpy import arange


# In[2]:


# get info about a function
get_ipython().run_line_magic('pinfo', 'np.sin')

# *args and **kwargs are mostly used in function definitions.
# *args and **kwargs allow you to pass a variable number of arguments to a function.
# *args is used to send a non-keyworded variable length argument list to the function.
# **kwargs allows you to pass keyworded variable length of arguments to a function.
# You should use **kwargs if you want to handle named arguments in a function.


# In[22]:


# Python prints only the last output in a cell automatically, so if you want to print more, use the function print

print(np.median([1,3,9]))
np.mean([7,3,4,6])


# In[30]:


# compute exponent
2**(-52)


# In[7]:


# taking out a range of values from array

# note that first index is always 0
xvalues = np.array([1, 0.1, 0.01, 0.001])
xvalues[1:3] # the latter number must be the index you want +1 
# returns values at index 1 and 2


# ## Loops and tests

# In[17]:


# for loop

for i in range(0,6):
    print(i)
    


# In[23]:


# while loop

a = 1
while a<10:
    print(a)
    a += 1


# In[1]:


# if test (in a function)

def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    elif score >= 50:
        letter = 'E'        
    else:
        letter = 'F'
    return letter

letterGrade(50)


# ## defining a function

# In[6]:


def E1(x):
    return (1-np.cos(x))/(np.sin(x)**2)

def E2(x):
    return 1/(1+np.cos(x))


# ex. of creating an error message if a condition is not satisfied:
# say we want to define f(x) = (x+1)/x only for x>0:
def f(x):
    if x < 0:
        raise ValueError('x is not positive')
    return (x+1)/x


# ## Applying a function to an array of values

# In[31]:


xvalues = np.array([1, 0.1, 0.01, 0.001])


# In[32]:


# using list comprehension
E1values = [E1(x) for x in xvalues]
E1values


# In[33]:


[(1-np.cos(x))/(np.sin(x)**2) for x in xvalues]


# In[34]:


# alternative:
list(map(E1, xvalues))
# r = map(func, seq) 
# map() returns an iterator. Use also function list() to make a list


# In[35]:


# another way to define a function, that is useful if the only use for it is in this line:
list(map(lambda x:(1-np.cos(x))/(np.sin(x)**2), xvalues))


# ## Plotting

# In[36]:


import matplotlib.pyplot as plt 
plt.plot(xvalues,E1values)


# In[43]:


# If you want to apply plotting options, I recommend creating a figure window first.
# The subplot function is useful even if we don't need subplots, because it gives an axes handle, here called "ax".
# "ax" is used in the following lines, where options are specified.
fig, ax = plt.subplots(figsize = [7,4])
nrange = np.arange(25,105,2)
ax.plot(xvalues,E1values,color="black",label="E1")
ax.legend(loc=2, prop={'size': 18})
ax.tick_params(axis='both',labelsize=22)
ax.set_xlim(0,1) 
ax.set_xlabel('x',fontsize = 18)
ax.set_ylabel('E1(x)',fontsize = 18)
ax.set_title('Example plot',fontsize = 18)
ax.grid()


# ## symbolic computing

# In[54]:


from sympy import *

x, y = symbols('x y')
def examplefunction(x,y):
    return x**2 + y**2

integrate(examplefunction(x,y),x)


# In[55]:


# substitute symbols with numbers:
examplefunction(x,y).subs(x,1)


# ## Use functions you have written in another notebook

# In[ ]:


# see https://stackoverflow.com/questions/44116194/import-a-function-from-another-ipynb-file

