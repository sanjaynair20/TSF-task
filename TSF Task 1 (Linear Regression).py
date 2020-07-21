#!/usr/bin/env python
# coding: utf-8

# # Simple Linear Regression
# 
# *In this regression task we will predict the percentage of marks that a student is expected to score based upon the number of hours they studied. This is a simple linear regression task as it involves just two variables.

# In[1]:


# Importing all libraries 
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


#importing data
url = "http://bit.ly/w-data"
marks = pd.read_csv(url)
print("Data imported successfully")


# In[8]:


marks


# In[9]:


marks.describe()


# In[17]:


#Plotting Values
marks.plot(x='Hours', y='Scores', style='x', c="red",fontsize=10)
plt.title('Hours vs Percentage',fontsize=10)
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()


# In[21]:


#Taking Values based on Index loc
X = marks.iloc[:, :-1].values
y = marks.iloc[:, 1].values
print(X)
print(y)


# In[55]:


#Reshapping Values to Array
x=marks["Hours"].values.reshape(-1, 1)
y=marks["Scores"].values.reshape(-1, 1)


# In[50]:


#Importing libraries for prediction
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[26]:


print(regressor.intercept_)


# In[56]:


print(regressor.coef_)


# In[29]:


y_pred = regressor.predict(X_test)


# In[31]:


#Creating new set with predicted values
marks1 = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
marks1


# In[59]:


#testing own data hours = 9.25
hours=np.array([9.25])
hours= hours.reshape(-1,1)
own_pred = regressor.predict(hours)
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))


# In[61]:


#Importing libraries to measure errors
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))


# In[65]:


# Plotting the regression line
line = regressor.coef_*X+regressor.intercept_



# Plotting for the test data
plt.scatter(X, y)
plt.plot(X, line);

plt.show()


# In[ ]:




