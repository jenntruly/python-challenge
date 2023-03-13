#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import csv
import os


# In[17]:


#read csv
csvpath =  os.path.join("election_data.csv")


# In[18]:


#open csv
with open(csvpath,encoding="utf8" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    df = pd.read_csv("election_data.csv")
    print(df.head())


# In[28]:


#The total number of votes cast

Total_Votes= len(df['Ballot ID'].unique())
print(Total_Votes)


# In[29]:


#A complete list of candidates who received votes and The total number of votes each candidate won

Candidates= df.pivot_table(index = ['Candidate'], aggfunc ='size')
print(Candidates)


# 

# In[30]:


# The percentage of votes each candidate won
percent= (Candidates/Total_Votes)*100
print(percent)


# In[31]:


#The winner of the election based on popular vote
winner= df['Candidate'].value_counts().idxmax()
print(winner)


# In[32]:


#set the output of the text file
text_path = "output.txt"


# In[33]:


with open(text_path, 'w') as file:
    file.write("Election Results\n")
    file.write("---------------------\n")
    file.write("Total Votes: %d\n" % Total_Votes)
    file.write("Candidates' total votes: $%d\n" % Candidates)
    file.write("Candidates' total percentage  $%d\n" % percent)
    file.write("Winner: %s ($%s)\n" % winner)


# In[ ]:




