#!/usr/bin/env python
# coding: utf-8

# In[92]:


import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


# In[115]:


x=np.linspace(-10,10,100)
y=4*x+5


# In[116]:


plt.axhline(y=0,color='k')
plt.axvline(x=0,color='k')
plt.grid()
plt.plot(x,y)


# In[117]:


x=[0,1,2]
y=[0,-2,-6]
plt.plot(x,y,color='red',linestyle='dashed',linewidth='7',marker='o',markerfacecolor='blue',markersize='12')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()


# In[110]:


marks=[1,2,3,4,5,6]
no_students=[5,7,18,9,5,2]
tick_label=['25','30','35','40','45','50']
plt.bar(marks,no_students,tick_label=tick_label,width=0.9,color=['green','red'])
plt.show()


# In[114]:


ages=[2,34,53,42,43,66,61,23,62,9,23,75,33,52,15,71,55,17,73,81,45,23,56,13,56,3,46,76]
range=(0,100)
bins=20
plt.hist(ages,bins,range,color='green',rwidth=0.8)
plt.show()


# In[ ]:




