# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:48:01 2024

@author: vines
"""

import pandas as pd
import matplotlib.pyplot as plt 

#%%

"""

Conjunto de datos extraído de: https://datos.gob.es/es/catalogo/a07002862-vacunacion-frente-a-la-gripe-por-edad-sexo-y-provincia-campana-24-25
 Licencia https://creativecommons.org/licenses/by/4.0/deed.es_ES
"""

series2 = pd.read_csv(
    
    "c:\\Users\\vines\\OneDrive\\Escritorio\\Master Data Science\\Visualizacion de datos\\PEC2\\segundo_grafico.csv",
    parse_dates=True,
    sep = ';',
    dayfirst=True
)

series2["fecha"]= pd.to_datetime(series2["fecha"])

data_plot= series2.pivot_table(
    index="fecha",
    columns="provincia",
    values="dosis_administradas",
    aggfunc="sum").fillna(0)


plt.figure()
plt.stackplot(data_plot.index, data_plot.T, labels=data_plot.columns)
plt.xticks(rotation=45)
plt.title(" Stream plot sobre la vacunación frente a la gripe ")
plt.xlabel("Fecha")
plt.ylabel("Dosis de vacunas administradas")
plt.tight_layout()
plt.legend()
