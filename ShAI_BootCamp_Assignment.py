#!/usr/bin/env python
# coding: utf-8

# #About Dataset
# salaries dataset generally provides information about the employees of an organization in relation to their compensation. It typically includes details such as how much each employee is paid (their salary), their job titles, the departments they work in, and possibly additional information like their level of experience, education, and employment history within the organization.

# # Features
# - 'Id'
# - 'EmployeeName'
# - 'JobTitle'
# - 'BasePay'
# - 'OvertimePay'
# - 'OtherPay'
# - 'Benefits'
# - 'TotalPay' -> salary
# - 'TotalPayBenefits'
# - 'Year'
# - 'Notes'
# - 'Agency'
# - 'Status'
# 

# # Tasks
# 
# 1. **Basic Data Exploration**: Identify the number of rows and columns in the dataset, determine the data types of each column, and check for missing values in each column.
# 
# 2. **Descriptive Statistics**: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
# 
# 3. **Data Cleaning**: Handle missing data by suitable method with explain why you use it.
# 
# 4. **Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.
# 
# 5. **Grouped Analysis**: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.
# 
# 6. **Simple Correlation Analysis**: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.
# 
# 8. **Summary of Insights**: Write a brief report summarizing the findings and insights from the analyses.

# # Very Important Note
# There is no fixed or singular solution for this assignment, so if anything is not clear, please do what you understand and provide an explanation.

# # Basic Data Exploration

# In[42]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[43]:


# Load your dataset
df = pd.read_csv('Salaries.csv')
df.head()


# In[44]:


df.columns


# In[45]:


print('number of rows and columns in the dataset',df.shape)


# * Identify the number of rows and columns in the dataset

# In[46]:


df.info()


# * determine the data types of each column  

# In[47]:


df.isnull().sum()


# * check for missing values in each column.

# * the coulmns **BasePay OvertimePay OtherPay Benefits TotalPay Notes Status** contain Null Values
# 
# # Descriptive Statistics

# In[48]:


df['TotalPay'].describe()


# * Calculate basic statistics mean, median, mode, minimum, and maximum salary,
# 

# In[76]:


df1=df[df['TotalPay']>0]

a=df1['TotalPay'].min()
b=df1['TotalPay'].max()

print(f'the Range of Salary from {a} to {b}')


# * determine the range of salaries, and find the standard deviation.

# # Data Cleaning

# * Handle missing data by suitable method with explain why you use it.

# In[50]:


df.isnull().sum()


# In[51]:


df


# In[52]:


df=df.fillna(0.0)


# In[53]:


df.isnull().sum()


# * I have filled [BasePay  OvertimePay	OtherPay	Benefits] the Null values of the columns with 0.0 because the Null value within these fields means that there is no money, whether in payment or Benefits.
# * filled [Notes	 Status]  Null Value her mean no Notes Or Status and the 0.0 value It has the same meaning but It has the same meaning but is easier to deal with
# * In my opinion, these two columns should be deleted because they do not provide any additional information
# 
# # Basic Data Visualization

# In[77]:


df1=df1['TotalPay']
df1.hist()

plt.title('Histogram of TotalPay')
plt.xlabel('TotalPay')
plt.ylabel('Frequency')
plt.show()


# * Create histograms or bar charts to visualize the distribution of salaries 

# In[55]:


department_counts=df['JobTitle'].value_counts()
department_counts


# In[16]:


# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(department_counts, labels=department_counts.index)
plt.title('Proportion of Employees in Different Departments')
plt.axis('equal')  
plt.show()


# # Grouped Analysis

# * Group the data by one or more columns and calculate summary statistics for each group,and compare the average salaries across different groups.

# In[28]:


grouped_data = df.groupby(['JobTitle', 'Year'])


# In[80]:


average_salary_by_group = grouped_data['TotalPay'].mean()
average_salary_by_group


# In[32]:


average_salary_by_group.unstack().plot(kind='bar', figsize=(12, 6), title='Average Salary Across Job Titles and Years')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.show()


# In[83]:


print(f'max Position Salary : {average_salary_by_group.idxmax()} \nmin Position Salary : {average_salary_by_group.idxmin()}')


# * use pie charts to represent the proportion of employees in different departments.

# # Simple Correlation Analysis

# * Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.

# In[35]:


correlation = df['TotalPay'].corr(df['BasePay'])
correlation


# In[41]:


numerical_column = 'BasePay'

plt.figure(figsize=(10, 6))
plt.scatter(df[numerical_column], df['TotalPay'])
plt.title(f'Scatter Plot: TotalPay vs {numerical_column}')
plt.xlabel(numerical_column)
plt.ylabel('TotalPay')
plt.show()


# # Good Luck!
