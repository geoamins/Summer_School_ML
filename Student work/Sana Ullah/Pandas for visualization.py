#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
# Create a DataFrame
data = {'Year': [2010, 2011, 2012, 2013, 2014,2015,2016,2017,2018],
        'Patients': [100, 120, 150, 200, 180,200,150,170,220]}
df = pd.DataFrame(data)
# Create a line plot
df.plot(x='Year', y='Patients', title='OPD Patients')


# In[11]:


import pandas as pd
# Create a DataFrame
data = {'District': ['Peshawar', 'Charsadda', 'Mardan', 'Bunir', 'Swabi'],
        'Patients': [8398748, 3980408, 2716000, 2326006, 5326000]}
df = pd.DataFrame(data)
# Create a bar plot
df.plot(x='District', y='Patients', kind='bar', title='Patients By District')


# In[21]:


import pandas as pd
# Create a DataFrame
data = {'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]}
df = pd.DataFrame(data)
# Create a histogram
df.plot(y='Age', kind='hist', bins=5, title='Age Distribution')


# In[19]:


import pandas as pd
# Create a DataFrame
data = {'District': ['Peshawar', 'Charsadda', 'Mardan', 'Bunir', 'Swabi'],
        'Patients': [8398748, 3980408, 2716000, 2326006, 5326000]}
df = pd.DataFrame(data)
# Create a scatter plot
df.plot(x='District', y='Patients', kind='scatter', title='Scatter Plot')


# In[20]:


import pandas as pd
# Create a DataFrame
#data = {'Category': ['A', 'B', 'C', 'D'],
 #       'Value': [30, 40, 20, 10]}
data = {'District': ['Peshawar', 'Charsadda', 'Mardan', 'Bunir', 'Swabi'],
        'Patients': [8398748, 3980408, 2716000, 2326006, 5326000]}
df = pd.DataFrame(data)
# Create a pie chart
df.plot(y='Patients', kind='pie', labels=df['District'], autopct='%1.1f%%', title='Category Distribution')


# In[ ]:




