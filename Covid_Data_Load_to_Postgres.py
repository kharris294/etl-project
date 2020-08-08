#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies

from bs4 import BeautifulSoup
from splinter import Browser
import requests
import re
import pandas as pd
from pprint import pprint
import pymongo


# In[17]:


executable_path = {'executable_path': r"C:\Users\jimkn\Downloads\chromedriver (7).exe"}
browser = Browser('chrome', **executable_path)


# In[ ]:





# In[18]:


# Locate website

url = 'https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home'
browser.visit(url)


# In[19]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[20]:



print(soup.prettify())


# In[21]:


element_number = soup.find_all(class_="stats-cards__number")
element_number


# In[22]:


#for element in element_number:
 #   print(element.get_text().strip())
numbers_list = [element.get_text().strip() for element in element_number]


# In[23]:


element_label = soup.find_all(class_="stats-cards__label")
element_label


# In[24]:


labels_list = [element.get_text().strip() for element in element_label]


# In[52]:


pd.DataFrame({"Labels" : labels_list, "Numbers" : numbers_list})
df


# In[45]:


import sqlalchemy
# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/ETL Project")
con = engine.connect()


# In[54]:


# Verify that there are no existing tables
print(engine.table_names())


# In[55]:


table_name = 'covid_data'
df.to_sql(table_name, con)


# In[56]:


print(engine.table_names())


# In[57]:


con.close()


# In[ ]:




