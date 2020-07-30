#!/usr/bin/env python
# coding: utf-8

# # TSF TASK-2
# Perform ‘Exploratory Data Analysis’ on the provided dataset ‘SampleSuperstore’

# In[20]:


# importing required packages
import pandas as pd
import pandas_profiling
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy.stats as stats


# In[4]:


#importing dataset
sam=pd.read_csv("SampleSuperstore.csv")
sam.head()


# In[14]:


sam.info()


# In[10]:


sam.describe()


# In[24]:


sam.shape


# In[36]:


#Removing duplicate rows
duplicate_rows_sam = sam[sam.duplicated()]


# In[38]:


sam.count()


# In[42]:


sam = sam.drop_duplicates()
sam.head(5)


# In[37]:


sam.tail(5)


# In[44]:


sam.count()


# In[9]:


# Finding the null values.
print(sam.isnull().sum())


# In[5]:


#This is the most simple step to get info about data
pandas_profiling.ProfileReport(sam)


# In[49]:


#finding correlation between values
sam.corr()


# In[15]:


#profit gained by each categories
(sam.groupby(['Category'])['Profit'].sum()/sam.groupby(['Category'])['Sub-Category'].count()).head()


# In[16]:


#Which consumers are frequent buyers
sam.groupby(['City'])['Segment'].count().reset_index().sort_values(by='Segment',ascending = False).head()


# In[19]:


#Which products have high discount rate
sam.groupby(['Category','Sub-Category'])['Discount'].describe().reset_index().sort_values(by = 'max', ascending = False).head()


# In[22]:


sam["Segment"].value_counts().plot(kind="bar")


# In[26]:


sam1=sam[['Sales','Quantity','Discount','Profit']]
sns.heatmap(sam.corr(),annot=True)


# In[30]:


#Here it can be observed that the sale of office supplies is way higher than that of the other two categories
sam['Category'].value_counts().plot(kind="bar")


# In[32]:


#Here the data is highly skewed
sns.distplot(sam["Sales"])


# In[33]:


#Here it can be seen that it is not necessary that with the increase in sale profit increases
sns.scatterplot("Sales",'Profit',data=sam)


# In[35]:


#Here it can be observed that profit decreases beyond 0.3 due to discounts
axes,fig=plt.subplots(0,1,figsize=(18,5))
sns.scatterplot("Discount",'Profit',data=sam)


# In[36]:


#The total sale amt is decreasing after some point
axes,fig=plt.subplots(0,1,figsize=(18,5))
sns.scatterplot('Sales','Discount',data=sam)


# In[38]:


#Arranged on the basis of most selling items
sam['Sub-Category'].value_counts().plot(kind="bar")


# In[55]:


#There is more profit in west and east
pd.crosstab(sam["Region"],sam["Category"],sam["Profit"],aggfunc='sum').plot(kind="bar",stacked=True)


# In[56]:


#Office supplies is the most selling category but the profit is highest from the technology sector 
pd.crosstab(index=sam["Category"],columns=sam["Segment"],values=sam["Profit"],aggfunc="sum").plot(kind="bar",stacked=True)


# In[58]:


pd.crosstab(index=sam["Category"],columns=sam["Ship_Mode"],values=sam["Profit"],aggfunc="sum").plot(kind="bar",stacked=True)


# In[60]:


#The profit is very low almost 0 in the Furniture sector also the profit is high in the Technology sector
sns.lmplot(x="Profit",y="Sales",data=sam,fit_reg=False,col="Category")
plt.show()


# In[62]:


#The profit is very high when the ship mode is Standard class
sns.lmplot(x="Profit",y="Sales",data=sam,fit_reg=False,col="Ship_Mode")


# In[63]:


#Profit is more for copiers in compared to other categories
axes,fig=plt.subplots(0,1,figsize=(18,5))
sns.barplot("Sub-Category","Profit",data=sam)


# # Observation
# 1.When the discount is till 0.3, there is a profit,But if the discount increases beyond 0.3 there is a loss happening
# 
# 2.Although office supplies is the most selling category but the profit is highest from the technology sector Under which the
# the profit has come more from the Consumers segment
# 
# 3.Although Copiers is the least selling sub-category but has given the most profit out of all the sub-categories.
# 
# 4.There is a huge loss from the furniture section
# 
# 5.The profit is more from the east and west region of the country.
# 

# # Suggestion for business
# 
# 1.The Discount should not be above 0.3.
# 
# 2.The Furniture category is causing the most loss, so its better to increase the price of the cost or try to reduce overall cost
# 
# 3."Same Day" Shipping rates should be increased
# 
# 4.Company should focus on tech section and try to concentrate on other sections too or there would be more loss in overall comparison 

# In[ ]:




