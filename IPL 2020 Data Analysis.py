#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


data=pd.read_csv('C:\\Users\\Vasundara\\Desktop\\Ipl_2020.csv')


# In[8]:


data


# In[9]:


data.count()


# In[10]:


data.isnull().sum()


# In[12]:


import seaborn as sn
import matplotlib.pyplot as plt


# In[13]:


sn.heatmap(data.isnull())
plt.show()


# In[3]:


import pandas as pd
data=pd.read_csv('C:\\Users\\Vasundara\\Desktop\\Ipl_2020.csv')


# In[4]:


data


# In[5]:


data.info()


# In[6]:


data.columns


# In[9]:


data.isnull().sum()


# ### Clean up data

# In[10]:


data=data.dropna(how='all')


# In[11]:


data.head()


# In[12]:


data.isnull().sum()


# ### Who wins the most matches

# In[13]:


data.groupby(['Match']).sum()


# In[16]:


data


# In[21]:


a=data.groupby(['winner']).sum()


# In[22]:


a


# ### Matches played by each team

# In[16]:


x=data['Team-1'].value_counts()
y=data['Team-2'].value_counts()
(x+y).plot(kind='barh')
print(x+y)


# In[35]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:



sns.countplot('winner',data=a)
plt.xticks(rotation='vertical')


# ### Top 5 Man of the Match players

# In[41]:


temp_data=a['player_of_the_match'].value_counts().head()
print(temp_data)
sns.barplot(x=temp_data.index,y=temp_data.values,data=a)
plt.title("Top 5 MOM")
plt.xticks(rotation=90)
plt.xlabel("Match Count")
plt.ylabel("Player")
plt.show()


# ### Which Team had won by maximum wickets?

# In[9]:


a=(data.iloc[data['win_by_wickets'].idxmax()]['winner'])


# In[10]:


print(a)


# In[11]:


a


# ### 6)	Which Team had won by minimum wickets?

# In[22]:


c=data.iloc[data[data['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# In[23]:


c


# In[32]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

frame=pd.read_csv('C:\\Users\\Vasundara\\Desktop\\Ipl_2020.csv')
frame


# ### Top 5 players of the match Winner

# In[51]:


top_player=frame.player_of_the_match.value_counts()[0:5]
fig,ax=plt.subplots()
ax.set_ylim([0,5])
ax.set_ylabel("Count")
ax.set_title("Top players of the match Winners")
sns.barplot(x=top_player.index,y=top_player,orient='v');
plt.show()


# ### Has toss Winning helped in winning matches?

# In[53]:


ss=frame['Toss Winner']==frame['winner']
ss.groupby(ss).size()


# In[54]:


sns.countplot(ss);


# In[ ]:




