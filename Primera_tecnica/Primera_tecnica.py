# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:32:43 2024

@author: vines
"""
import pandas as pd
import matplotlib.pyplot as plt 
#%%

"""

Conjunto de datos extraído de: https://datos.gob.es/es/catalogo/l01280066-accidentes-de-trafico-en-alcobendas-desde-el-ano-2020
Open Data Commons Attribution License (ODC-By) Summary

This is a human-readable summary of the ODC-BY 1.0 license. Please see the disclaimer below.

You are free:

To share: To copy, distribute and use the database.
To create: To produce works from the database.
To adapt: To modify, transform and build upon the database.
As long as you:

Attribute: You must attribute any public use of the database, or works produced from the database, in the manner specified in the license. For any use or redistribution of the database, or works produced from it, you must make clear to others the license of the database and keep intact any notices on the original database.
Disclaimer

This is not a license. It is simply a handy reference for understanding the ODC-BY 1.0 — it is a human-readable expression of some of its key terms. This document has no legal value, and its contents do not appear in the actual license. Read the full ODC-BY 1.0 license text for the exact terms that apply.   

"""

series1 = pd.read_csv(
    
    "c:\\Users\\vines\\OneDrive\\Escritorio\\Master Data Science\\Visualizacion de datos\\PEC2\\primer_grafico.csv",
    index_col=0,
    parse_dates=True,
    #squeeze=True,
    sep = ',',
    dayfirst=True
)

accidentes_año= series1.groupby("Año").size()

plt.figure()
plt.pie(accidentes_año, labels=accidentes_año.index, autopct='%.2f')
plt.title("Pier chart que representa el nº de accidentes de tráfico en Alcobendas desde el año 2020")
plt.tight_layout()
plt.show()