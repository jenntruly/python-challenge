#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
import os
import csv
import numpy as np


# In[80]:


#read csv
csvpath =  os.path.join("budget_data.csv")


# In[81]:


#open csv
with open(csvpath,encoding="utf8" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    df = pd.read_csv("budget_data.csv")
    print(df.head())


# In[82]:


#Find the total number of months
Total_Months= len(df['Date'].unique())
print(Total_Months)


# In[83]:


#Find the net total amount of "Profit/Losses" over the entire period
Total= df["Profit/Losses"].sum()
print(Total)


# In[84]:


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
df['shifted']= df["Profit/Losses"].shift(1)
df["growth"]=df["Profit/Losses"]-df['shifted']
Average_change= round(df["growth"].mean(),2)
print(Average_change)


# In[85]:


#The greatest increase in profits (date and amount) over the entire period
greatest_increase= int(df["growth"].max())
print(greatest_increase)
rowNumIncrease=df[df["growth"]== greatest_increase].index
monthIncrease= df['Date'][rowNumIncrease]
print(monthIncrease)


# In[86]:


#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease= int(df["growth"].min())
print(greatest_decrease)
rowNumDecrease= df[df["growth"]== greatest_decrease].index
monthDecrease= df['Date'][rowNumDecrease]
print(monthDecrease)


# In[87]:


#set the output of the text file
text_path = "output.txt"


# In[88]:


with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % Total_Months)
    file.write("Total Revenue: $%d\n" % Total)
    file.write("Average Revenue Change $%d\n" % Average_change)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (monthIncrease, greatest_increase))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (monthDecrease, greatest_decrease))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




