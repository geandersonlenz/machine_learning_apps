
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import _pickle as cPickle
import requests, json


# In[2]:


df = pd.read_csv('top_products.csv')


# In[3]:


x = df.iloc[:, 4:]
y = df.iloc[:, :4]


# In[4]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)


# In[5]:


forest = RandomForestClassifier(n_estimators=100, random_state=1)
classifier = MultiOutputClassifier(forest, n_jobs=-1)
classifier.fit(X_train, y_train)


# In[16]:


classifier.predict([[10, 12, 1, 350, 3]])


# In[6]:


cPickle.dump(classifier, open("top_product.pkl", "wb"))

