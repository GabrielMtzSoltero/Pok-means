# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:13:43 2023

@author: GabrielMtz
"""
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import sys
#leer el archivo
dataFilePath = '../datasets/Po_k_means2.csv'
etiquetaX='Hp'
etiquetaY='Att'
df = pd.read_csv(dataFilePath)
colores=['r','g','b']
fig, ax = plt.subplots()
ax.scatter(df[etiquetaX], df[etiquetaY])


ax.set_xlabel(etiquetaX)
ax.set_ylabel(etiquetaY)
cantPokemon=df.shape[0]
for i in range(cantPokemon):   
    ax.annotate(df['Pokemon'].iloc[i], (df[etiquetaX].iloc[i], df[etiquetaY].iloc[i]))
# ax.annotate(df['Pokemon'], df[[etiquetaX,etiquetaY]].to_numpy())
Kernels=np.array([[288,335],[440,360],[295,310]]).astype(float)
Kernels=np.array([[335,288],[360,440],[310,295]]).astype(float)
grupo=np.ones(cantPokemon)*sys.float_info[0]
grupo=np.ones(cantPokemon)
df['grupo']=grupo
print(df[etiquetaX].min())
print(df[etiquetaX].max())
ite=3
kernelHist=[[[288,335]],[[440,360]],[[295,310]]]
kernelHist=[[[335,288]],[[360,440]],[[310,295]]]
kernelHistNP=np.array(kernelHist,dtype=object)
for i in range(ite):
    #plotear los centroides
    ax.plot(kernelHistNP[0,:,0],kernelHistNP[0,:,1],'-*r')
    ax.plot(kernelHistNP[1,:,0],kernelHistNP[1,:,1],'-*g')
    ax.plot(kernelHistNP[2,:,0],kernelHistNP[2,:,1],'-*b')
    # Asignar un grupo a cada pokemon
    for pokemonIdx in range(cantPokemon):
        disAnt=sys.float_info[0]
        for idx,k in enumerate(Kernels):
                dis=np.linalg.norm([df[etiquetaX].iloc[pokemonIdx]-k[0],df[etiquetaY].iloc[pokemonIdx]-k[1]])                
                if(dis<disAnt):
                    disAnt=dis
                    df['grupo'].iloc[pokemonIdx]=idx
    # Mover los centroides
    ax.scatter(df[etiquetaX], df[etiquetaY],c=df['grupo'])
    for idx,k in enumerate(Kernels):
        filter1 = df["grupo"]==idx
        moveX=df.where(filter1)[etiquetaX].mean()
        moveY=df.where(filter1)[etiquetaY].mean()
        Kernels[idx,:]=np.array([moveX,moveY])
        kernelHist[idx].append([moveX,moveY])
        kernelHistNP=np.array(kernelHist,dtype=object)
    
ax.set_xlim(200,550)
ax.set_ylim(180,450)
# plt.setp(ax, xlim=(200,450), ylim=(250,550))
print(ax.get_xlim())
print(ax.get_ylim())
