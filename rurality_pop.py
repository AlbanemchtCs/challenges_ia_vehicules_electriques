# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:23:14 2023

@author: Admin
"""

import pandas as pd

def f(x):
    
    if x == 'rural autonome très peu dense':
        return 0
    elif x == 'rural autonome peu dense':
        return 1
    elif x == "rural sous faible influence d'un pôle":
        return 2
    elif x == "rural sous forte influence d'un pôle":
        return 3
    elif x == 'urbain densité intermédiaire':
        return 4
    elif x == 'urbain dense':
        return 5
    

Rural = pd.read_csv('C:/Users/Admin/Downloads/CSV_ruralité.csv',sep=';')
Population = pd.read_csv('C:/Users/Admin/Downloads/CSV_Pop.csv',sep=';',dtype={'codgeo' : str})
Population = Population[Population['an']== 2018].rename(columns = {'p_pop' : 'population'})
Rural = Rural.rename(columns = {'Code géographique communal' : 'codgeo'})
Tot = pd.merge(Population,Rural,on='codgeo').drop(columns = 'an')

Tot['rurality'] = Tot['Typologie urbain/rural'].apply(f)

Result = Tot.drop(columns=['Typologie urbain/rural','libgeo']).dropna().astype({'population' : int})

