#!/usr/bin/env python
# coding: utf-8

# 1 . Find out how many male and female passenger was onboarded .
# 2. how many survived we have .
# 3. how many casuality we have 
# 4 . what is name of a person who is the eldest one . 
# 5 . how many passenger do we have in first , second and third class 
# 6. how many person we have whose name starts with "s"
# 7. try to create a new column which is a summation  of "SibSp" and "parch"
# 8 . how many person do we have below age of 25 .
# 9 . how many person died whose age was less then 40 
# 10 . from a  cabin column seperate text and numeric value . 
# 

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[3]:


df


# In[6]:


q=df.describe()


# In[7]:


q


# In[8]:


q1=df['Sex']


# In[10]:


q1.describe()


# male=577
# female=891-577
# =314

# In[14]:


q2=df['Survived']==True


# In[15]:


q2


# In[16]:


q2.describe()


#  survived=891-549
#         =342

# In[18]:


q4=df[['Name', 'Age']]


# In[19]:


q4


# In[21]:


q4.describe()


# In[23]:


q4.sort_values('Age')


# Thomas,Master .Assad Alexander  with .42 age 

# In[25]:


q5=df['Pclass']


# In[27]:


q5.describe()


# In[28]:


df['Pclass'].value_counts()


# In[52]:


q6=df['Name']


# In[53]:


q6.describe()


# In[54]:


q6


# In[58]:


q6=df.sort_values('Name',ascending=True)


# In[59]:


q6


# In[60]:


q61=q6['Name']


# In[62]:


q61.describe()


# In[67]:


q6.info()


# In[ ]:


Q7


# In[112]:



df['SibSp&Parch']=df['SibSp']+df['Parch']


# In[113]:


df


# In[73]:


q8= df['Age']<25 


# In[74]:


q8.describe()


# below 25 is 891-613= 278

# In[81]:


q9=df[['Age', 'Survived']]


# In[84]:


q91=df['Age']<40 & df['Survived']


# In[86]:


q91.describe()


# In[108]:


q11=df['Age']<40
q21=df['Survived']==False
q9=df[q11&q21]


# In[109]:


q9


# No of peoples below 40&not survived=322

# In[126]:


q10=df['Cabin']


# In[127]:


q10


# In[ ]:





# In[ ]:




