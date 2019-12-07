#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt


# In[34]:


total_ksa = pd.read_excel('physicians_and_dentists_in_ksa.xlsx', header = 5, usecols = [1,14,15,16,17],index_col=0)

# use this to remove the number  in the column name
total_ksa = total_ksa.rename(columns={col: col.split('.')[0] for col in total_ksa.columns})
total_ksa.head()


# In[35]:


moh = pd.read_excel('physicians_and_dentists_in_ksa.xlsx', header = 5, usecols = [1,2,3,4,5],index_col=0)
moh.head()


# In[36]:


gov = pd.read_excel('physicians_and_dentists_in_ksa.xlsx', header = 5, usecols = [1,6,7,8,9],index_col=0)
gov = gov.rename(columns={col: col.split('.')[0] for col in gov.columns})
gov.head()


# In[37]:


private = pd.read_excel('physicians_and_dentists_in_ksa.xlsx', header = 5, usecols = [1,10,11,12,13],index_col=0)
private = private.rename(columns={col: col.split('.')[0] for col in private.columns})
private.head()


# In[30]:


def mean_profession(df,profession,sector):
    
    meanProfession = df[profession].mean()

    print(f'The average {profession} per Speciality on {sector} is {meanProfession:.3f}.')


# In[31]:


# 1. The average of Consultants   they  work in MOH
mean_profession(moh,'Consultant','MOH')

# 2.The average of  consultant they work private sector 
mean_profession(private,'Consultant','Private')

# 3.The  average of consultant they work in Other Governmental Sector
mean_profession(gov,'Consultant','Other Governmental Sector')


# In[45]:


# 4.The average of consulant in  Anaesthesia  in all sectores  ( MOH – Private sector -Other Governmental Sector

df = private.copy()
df = df.merge(moh,suffixes=('_private','_moh'),left_index=True,right_index=True)
df = df.merge(gov,left_index=True,right_index=True)
df = df.rename(columns={col: col+'_gov' for col in df.columns if '_' not in col})
df = df.merge(total_ksa,left_index=True,right_index=True)
df = df.rename(columns={col: col+'_ksa' for col in df.columns if '_' not in col})
df.head()


# In[49]:


# Continue #4
print('The number of consultants in each sector that are in Anaesthesia')
display(df[['Consultant_private','Consultant_moh','Consultant_gov','Consultant_ksa']].loc['Anaesthesia'])

print('The average number number of consultants that are in Anaesthesia for all sectors = ',
    df[['Consultant_private','Consultant_moh','Consultant_gov','Consultant_ksa']].loc['Anaesthesia'].mean())


# In[50]:


df.describe()


# In[56]:


df.hist(figsize = (15,10))


# In[61]:


df['Consultant_gov'].plot.bar(figsize=(15,5))







