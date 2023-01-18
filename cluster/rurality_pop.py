# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 09:23:14 2023

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def convert_rurality(x):
    
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
Centroide = pd.read_csv('C:/Users/Admin/Downloads/GEO_TER_ADE_centroide_communes_france.csv',sep=';',dtype={'insee_com' : str}).rename(columns = {'insee_com' : 'codgeo',
                                                                                                                                'X_COORD' : 'longitude',
                                                                                                                                'Y_COORD' : 'latitude'})[['codgeo','latitude','longitude']]
Bucks = pd.read_csv('C:/Users/Admin/Downloads/FRANCE_COMMUNE_NIVEAU_DE_VIE-FIGARO.csv',sep=';',dtype={'CODGEO' : str}).rename(columns = {'CODGEO' : 'codgeo',
                                                                                                                                        'MED14' : 'com_life_level'})
Population = Population[Population['an']== 2018].rename(columns = {'p_pop' : 'population'})
Rural = Rural.rename(columns = {'Code géographique communal' : 'codgeo'})
Tot = pd.merge(Population,Rural,on='codgeo').drop(columns = 'an')
Tot = Tot.merge(Centroide,on='codgeo')
Tot = Tot.merge(Bucks,on='codgeo')
Tot['rurality'] = Tot['Typologie urbain/rural'].apply(convert_rurality)

Result = Tot.dropna().astype({'population' : int,'com_life_level':float})
#Result.to_csv('C:/Users/Admin/Downloads/data_commune.csv')
#plt.hist(Result[Result['population'] < 1000]['population'],bins=30)