# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:50:39 2023

@author: Admin
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import kMeans
data = pd.read_csv('C:/Users/Admin/Downloads/data_commune.csv')

kmeans = KMeans(n_clusters=100)
kmeans.fit(data[['population','rurality','longitude','latitude']])