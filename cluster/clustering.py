# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 14:50:39 2023

@author: Admin
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
data = pd.read_csv('C:/Users/Admin/Downloads/data_commune.csv')
inputs = data[['population','rurality','com_life_level','longitude','latitude']]
scaler = StandardScaler().fit(inputs)
inputs = scaler.transform(inputs)

"""
L_inertia = []
for i in range(6,100):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(inputs)
    L_inertia.append(kmeans.inertia_)




plt.plot(L_inertia)

"""

kmeans = KMeans(n_clusters=40)
kmeans.fit(inputs)
data['cluster'] = kmeans.predict(inputs)
data = data.drop(columns=['Unnamed: 0','LIBGEO'])
#plt.scatter(data['longitude'],data['latitude'],c=data['cluster'])
paris_cluster = int(data[data['codgeo']== '75056']['cluster'])

filt  = data[np.sqrt((data['latitude']-float(data[data['codgeo']== '75056']['latitude']))**2+
             (data['longitude']-float(data[data['codgeo']== '75056']['longitude']))**2) < 15000]
plt.scatter(filt['longitude'],filt['latitude'],c=filt['cluster'])

data.to_csv('C:/Users/Admin/Downloads/data_commune_cluster.csv')
