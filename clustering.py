#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:05:04 2018

@author: abhik
"""

import pandas as pd

def compute():
  data_crop = pd.read_csv("crop_production.csv")

  data_weather = pd.read_csv("weathe_data.csv",parse_dates=True, index_col= 'timestamp')
  data_weather =  data_weather.drop('id',axis=1)


  dataTN=data_crop[data_crop.State_Name=='Tamil Nadu']
  dataAP=data_crop[data_crop.State_Name=='Andhra Pradesh']
  dataP=data_crop[data_crop.State_Name=='Puducherry']


  dataPondi=dataP[dataP.District_Name=='PONDICHERRY']
  dataPondi=dataPondi.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataPondi=dataPondi.groupby('Crop')['Production'].sum()
  dataPondi = pd.DataFrame({'crop':dataPondi.index, 'value':dataPondi.values}) 
  dataPondi=dataPondi.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataPondi['place']='Puducherry'
  dataPondi['water']=7


  dataAP.District_Name.unique()
  dataAP_WestG=dataAP[dataAP.District_Name=='WEST GODAVARI']
  dataAP_WestG=dataAP_WestG.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataAP_WestG=dataAP_WestG.groupby('Crop')['Production'].sum()
  dataAP_WestG = pd.DataFrame({'crop':dataAP_WestG.index, 'value':dataAP_WestG.values}) 
  dataAP_WestG=dataAP_WestG.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataAP_WestG['place']='West Godavari'
  dataAP_WestG['water']=6

  dataAP_Guntur=dataAP[dataAP.District_Name=='GUNTUR']
  dataAP_Guntur=dataAP_Guntur.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataAP_Guntur=dataAP_Guntur.groupby('Crop')['Production'].sum()
  dataAP_Guntur = pd.DataFrame({'crop':dataAP_Guntur.index, 'value':dataAP_Guntur.values}) 
  dataAP_Guntur=dataAP_Guntur.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataAP_Guntur['place']='Guntur'
  dataAP_Guntur['water']=7

  dataAP_Prakasam=dataAP[dataAP.District_Name=='PRAKASAM']
  dataAP_Prakasam=dataAP_Prakasam.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataAP_Prakasam=dataAP_Prakasam.groupby('Crop')['Production'].sum()
  dataAP_Prakasam = pd.DataFrame({'crop':dataAP_Prakasam.index, 'value':dataAP_Prakasam.values}) 
  dataAP_Prakasam=dataAP_Prakasam.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataAP_Prakasam['place']='Prakasam'
  dataAP_Prakasam['water']=6


  dataAP_Krishna=dataAP[dataAP.District_Name=='KRISHNA']
  dataAP_Krishna=dataAP_Krishna.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataAP_Krishna=dataAP_Krishna.groupby('Crop')['Production'].sum()
  dataAP_Krishna = pd.DataFrame({'crop':dataAP_Krishna.index, 'value':dataAP_Krishna.values}) 
  dataAP_Krishna=dataAP_Krishna.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataAP_Krishna['place']='Krishna'
  dataAP_Krishna['water']= 8

  dataAP_Nellore=dataAP[dataAP.District_Name=='SPSR NELLORE']
  dataAP_Nellore=dataAP_Nellore.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataAP_Nellore=dataAP_Nellore.groupby('Crop')['Production'].sum()
  dataAP_Nellore = pd.DataFrame({'crop':dataAP_Nellore.index, 'value':dataAP_Nellore.values}) 
  dataAP_Nellore=dataAP_Nellore.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataAP_Nellore['place']='Nellore'
  dataAP_Nellore['water']=6

  dataAP_Chitoor=dataAP[dataAP.District_Name=='CHITTOOR']
  dataAP_Chitoor=dataAP_Chitoor.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataAP_Chitoor=dataAP_Chitoor.groupby('Crop')['Production'].sum()
  dataAP_Chitoor = pd.DataFrame({'crop':dataAP_Chitoor.index, 'value':dataAP_Chitoor.values}) 
  dataAP_Chitoor=dataAP_Chitoor.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataAP_Chitoor['place']='Chittoor'
  dataAP_Chitoor['water']=7

  dataTN_Kanchipuram=dataTN[dataTN.District_Name=='KANCHIPURAM']
  dataTN_Kanchipuram=dataTN_Kanchipuram.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataTN_Kanchipuram=dataTN_Kanchipuram.groupby('Crop')['Production'].sum()
  dataTN_Kanchipuram = pd.DataFrame({'crop':dataTN_Kanchipuram.index, 'value':dataTN_Kanchipuram.values}) 
  dataTN_Kanchipuram=dataTN_Kanchipuram.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataTN_Kanchipuram['place']='Kanchipuram'
  dataTN_Kanchipuram['water']=3


  dataTN_Thiruvallur=dataTN[dataTN.District_Name=='THIRUVALLUR']
  dataTN_Thiruvallur=dataTN_Thiruvallur.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataTN_Thiruvallur=dataTN_Thiruvallur.groupby('Crop')['Production'].sum()
  dataTN_Thiruvallur = pd.DataFrame({'crop':dataTN_Thiruvallur.index, 'value':dataTN_Thiruvallur.values}) 
  dataTN_Thiruvallur=dataTN_Thiruvallur.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataTN_Thiruvallur['place']='Thiruvallur'
  dataTN_Thiruvallur['water']=7


  dataTN_Villupuram=dataTN[dataTN.District_Name=='VILLUPURAM']
  dataTN_Villupuram=dataTN_Villupuram.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataTN_Villupuram=dataTN_Villupuram.groupby('Crop')['Production'].sum()
  dataTN_Villupuram = pd.DataFrame({'crop':dataTN_Villupuram.index, 'value':dataTN_Villupuram.values}) 
  dataTN_Villupuram=dataTN_Villupuram.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataTN_Villupuram['place']='Viluppuram'
  dataTN_Villupuram['water']=5


  dataTN_Cuddalore=dataTN[dataTN.District_Name=='CUDDALORE']
  dataTN_Cuddalore=dataTN_Cuddalore.drop(['State_Name','Crop_Year','Season'],axis=1)
  dataTN_Cuddalore=dataTN_Cuddalore.groupby('Crop')['Production'].sum()
  dataTN_Cuddalore = pd.DataFrame({'crop':dataTN_Cuddalore.index, 'value':dataTN_Cuddalore.values}) 
  dataTN_Cuddalore=dataTN_Cuddalore.sort_values(by="value",axis=0,ascending=[False])[:10]
  dataTN_Cuddalore['place']='Cuddalore'
  dataTN_Cuddalore['water']=7




  data_totalCrops=dataPondi.append([dataPondi,dataAP_WestG,dataAP_Guntur,dataAP_Prakasam,dataAP_Krishna,dataAP_Nellore,dataAP_Chitoor,dataTN_Kanchipuram,
  dataTN_Thiruvallur,dataTN_Villupuram,dataTN_Cuddalore])

  data_location = pd.read_csv("latlonplaceupdated.csv")

  data_cropLocation = pd.merge(data_totalCrops, data_location, on=['place'])

  data_soil = pd.read_csv("soil_profile.csv")
  data_soil =  data_soil.drop('id',axis=1)

  ###############################################################################
  data_soil.SNDPPT=data_soil.SNDPPT.astype('float64')
  data_soil.SLTPPT=data_soil.SLTPPT.astype('float64') 
  data_soil.CLYPPT=data_soil.CLYPPT.astype('float64')
  data_soil.PHIHOX=data_soil.PHIHOX.astype('float64')
  data_soil.AWCH1=data_soil.AWCH1.astype('float64')
  data_soil.ALUM3S=data_soil.ALUM3S.astype('float64')
  data_soil.dtypes
  data_soil.columns = map(str.lower, data_soil.columns) 

  ###############################################################################


  data_soilcropLocation = pd.merge(data_soil,data_cropLocation, on=['lat','lon'])

  data_soilcropLocation=data_soilcropLocation.drop('place',axis=1)

  #Cli
  data_soilcropLocation = pd.merge(data_weather, data_soilcropLocation, on=['lat','lon'])
  data_soilcropLocation[-1]=data_soilcropLocation['crop']
  data_soilcropLocation=data_soilcropLocation.drop('crop',axis=1)
  data_soilcropLocation['crop']=data_soilcropLocation[-1]
  data_soilcropLocation=data_soilcropLocation.drop(-1,axis=1)
  cropList = list(data_soilcropLocation.crop.unique())
  pandasList=[]
  for i in cropList:
      sample = data_soilcropLocation[data_soilcropLocation.crop==str(i)]
      pandasList.append(sample)
      
      
  import numpy as np
  import matplotlib.pyplot as plt
  from sklearn.preprocessing import StandardScaler
  from sklearn.cluster import KMeans

  for df in pandasList:
      try:
         X = df.iloc[:,:-1].values
         #y = df.iloc[:,].values
         if(X.shape[0]<5):
             pass
         wcss = []
         sc_X = StandardScaler()
         X = sc_X.fit_transform(X)
         for i in range(1, 11):
             kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
             kmeans.fit(X)
             wcss.append(kmeans.inertia_)
         plt.plot(range(1, 11), wcss)
         plt.title('The Elbow Method')
         plt.xlabel('Number of clusters')
         plt.ylabel('WCSS')
         plt.show()
         kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)
         y_kmeans = kmeans.fit_predict(X)
         plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
         plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
         plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
         plt.title('Clusters of vegetables')
         plt.legend()
         plt.show()
      except ValueError:
          print('Non-numeric data found in the file.')
          
          

          
          
  X = data_soilcropLocation.iloc[:,:-1].values
  #y = df.iloc[:,].values
  wcss = []
  sc_X = StandardScaler()
  X = sc_X.fit_transform(X)
  for i in range(1, 11):
      kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
      kmeans.fit(X)
      wcss.append(kmeans.inertia_)
  plt.plot(range(1, 11), wcss)
  plt.title('The Elbow Method')
  plt.xlabel('Number of clusters')
  plt.ylabel('WCSS')
  plt.show()
  kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
  y_kmeans = kmeans.fit_predict(X)
  plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
  plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
  plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
  plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
  plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
  plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
  plt.title('Clusters of vegetables')
  plt.legend()
  plt.show()







  X_check = np.array([14.75,    0.0012,    0.03,    76.41,    0.8    ,1010.06,    14.81,    0.89,    7    ,277.34,    80.5,    10,    12,    14,    2,    5,    45,    227445,15])


  X_scaled = sc_X.transform(X_check.reshape(1,-1))
  centroid=kmeans.predict(X_scaled)
  dis=kmeans.cluster_centers_[centroid]

  water = sc_X.inverse_transform(dis-X_scaled)


  water_req = water[0][18]/X_check[18]
  print(water_req*100)