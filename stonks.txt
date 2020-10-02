#!/usr/bin/env python
# coding: utf-8

# In[181]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[172]:


Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
spy = pd.read_csv('spy.csv', index_col='Month')
p = spy.iloc[0:5031]


# In[177]:


a = ((p['Close'] - p['Open'])/p['Open'])

b = []

b.append(a.loc['January'].mean())
b.append(a.loc['February'].mean())
b.append(a.loc['March'].mean())
b.append(a.loc['April'].mean())
b.append(a.loc['May'].mean())
b.append(a.loc['June'].mean())
b.append(a.loc['July'].mean())
b.append(a.loc['August'].mean())
b.append(a.loc['September'].mean())
b.append(a.loc['October'].mean())
b.append(a.loc['November'].mean())
b.append(a.loc['December'].mean())

d = {'Month':Months, 'Avg Return': b}
df = pd.DataFrame(d)
df


# In[193]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(Months,b)
plt.show()


# In[ ]:




