# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:45:18 2024

@author: vines
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#%%
series3 = pd.read_csv(
    
    "c:\\Users\\vines\\OneDrive\\Escritorio\\Master Data Science\\Visualizacion de datos\\PEC2\\Tercera_tecnica\\data\\tercer_grafico.csv",
    parse_dates=True,
    sep = ';',
    dayfirst=True
)

series3["Total"]=pd.to_numeric(series3["Total"].str.replace(".","", regex=False).str.replace(",","."), errors="coerce")

data_final=series3.groupby(["Periodo", "Continentes"], as_index=False).mean()

# poner periodo como indice y continentes como columnas

data_final=data_final.pivot(index="Periodo", columns="Continentes", values="Total")

# Eliminar valores faltantes para que no hayan errores

data_final=data_final.dropna()

#%% Creación del horizon plot

bandas_colores= 4

cmap= plt.cm.coolwarm

colores_positivos=[cmap(i/bandas_colores) for i in range(bandas_colores)]
colores_negativos=[cmap(i/bandas_colores) for i in range(bandas_colores,0,-1)]

fig, ax=plt.subplots()
for i, (continente, valores) in enumerate(data_final.items()):
    
    #Normalización de valores para una mejor visualización
    valor_maximo=np.amax((np.abs(valores)))
    paso= valor_maximo/bandas_colores
    posicion_y= np.arange(len(valores))
    
    for b in range (bandas_colores):
        
        banda_alta= paso * (b+1)
        banda_baja= paso*b
        
        valores_banda= valores.clip(lower=banda_baja, upper=banda_alta)- banda_baja
        ax.fill_between(posicion_y, i, i + valores_banda/valor_maximo, color= colores_positivos[b])
        
        valores_banda= -valores.clip(lower=-banda_baja, upper=-banda_alta)- banda_baja
        ax.fill_between(posicion_y, i, i - valores_banda/valor_maximo, color= colores_negativos[b])
        
        

leyenda=[ plt.Line2D([0], [0], color=colores_positivos[0], lw=4, label="Gasto medio muy elevado"),
         plt.Line2D([0], [0], color=colores_positivos[1], lw=4, label="Gasto medio elevado"),
         plt.Line2D([0], [0], color=colores_negativos[0], lw=4, label="Gasto medio bajo"),
         plt.Line2D([0], [0], color=colores_negativos[1], lw=4, label="Gasto medio muy bajo")]

ax.set_yticks(range(len(data_final.columns)))
ax.set_yticklabels(data_final.columns, rotation=45)
ax.set_xticks(range(len(data_final.index)))
ax.set_xticklabels(data_final.index, rotation=45)
ax.set_title("Horizon plot del gasto medio por continete")

ax.legend(handles=leyenda, loc="upper right")
plt.tight_layout()
plt.show()


        
        
        
        
        