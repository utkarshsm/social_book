#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[8]:


record = { 
  
 'Name' : ['Ankit', 'Swapnil', 'Aishwarya', 
          'Priyanka', 'Shivangi', 'Shaurya' ],
    
 'Age' : [22, 20, 21, 19, 18, 22], 
    
 'Stream' : ['Math', 'Commerce', 'Science', 
            'Math', 'Math', 'Science'], 
    
 'Percentage' : [90, 90, 96, 75, 70, 80] } 
    


# In[9]:


data = pd.DataFrame(record,
                         columns = ['Name', 'Age', 
                                    'Stream', 'Percentage']) 


# In[10]:


data


# In[15]:


data1 = data[data['Percentage'] > 80]


# In[16]:


data1


# In[20]:


display(data.query('Age  >= 20 & Percentage > 80 '))


# In[22]:


print(data.replace('Ankit', 'Utkarsh'))


# In[23]:


record1 = { 
  
 'Name' : ['Ankit', 'hello', 'Aishwarya', 
          'Priyanka', 'dummy', 'Shaurya' ],
    
 'Age' : [22, 34, 21, 54, 18, 22], 
    
 'Stream' : ['Math', 'Commerce', 'Science', 
            'Math', 'Math', 'Science'], 
    
 'Percentage' : [90, 76, 96, 75, 70, 80] } 


# In[26]:


data3 = pd.DataFrame(record1,
                         columns = ['Name', 'Age', 
                                    'Stream', 'Percentage']) 


# In[27]:


data3


# In[29]:


fdata = data.append(data3)


# In[30]:


fdata


# In[ ]:




