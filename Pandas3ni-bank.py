#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bf=pd.read_csv('C:\\Users\\Windows\\Desktop\\Ak\\bank.csv' ,sep=";")


# In[3]:


bf


# In[4]:


bf['campaign']


# In[5]:


q1=pd.DataFrame(bf['campaign'])


# In[13]:


q1


# In[7]:


bf[['housing', 'loan']]


# In[ ]:





# In[8]:


q3=pd.DataFrame(bf['age']>30)


# In[9]:


q3


# In[10]:


len(q3)


# In[11]:


q3.describe()


# In[ ]:


bf.describe()


# In[15]:


q2=bf[['housing', 'loan']]


# In[16]:


q2


# In[17]:


q2.describe()


# q4. in which month we have trageted most of the customer . 

# In[18]:


q4=bf[['month', 'campaign']]


# In[19]:


q4.describe()


# In[20]:


q4


# q5.which mode of call is giving you more result

# In[21]:


q5=bf[['contact', 'y']]


# In[22]:


q5.describe()


# q6.how many enterpeures do we have in this list 

# In[23]:


q6=bf['loan']


# In[24]:


q6.describe()


# q7.how many customers do we have with negative balance 

# In[25]:


q7=bf['balance'] <0


# In[26]:


q7.describe()


# q8.prepare a group of data based on education level . 

# In[27]:


q8=bf[['education','default','balance','housing','loan','contact','day','month','duration','campaign','pdays','previous','poutcome','y']]


# In[28]:


q8


# In[29]:


q8.describe()


# In[ ]:




