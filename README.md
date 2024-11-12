# PEC2_Visualicacion_de_datos
Repositorio para publicar los diferentes resultados obtenidos a través del análisis de los tres datasets analizados para esta PEC.

La siguiente práctica se basa en la creación de diferentes codigos de Python con el fin de represetnar tres técnicas específicas de visualizaciónd e datos:

De este modo, el objetivo de esta práctica consta en desarrollar un conjunto de scripts de Python, que permita resolver diferentes cuestiones que se irán abordando. Para la realización
del código que se organiza de manera lógica separando por diferentes archivos planos .py por ejercicios de tal modo que existen un total de **3 archivos planos**

- Primera_tecnica.py

- Segunda_tecnica.py

- Tercera_tecnica.py

Cada uno de estos archivos planos consta de diferentes líneas de codigo que permiten analizar el conjunto de datos, hacer una primera base de preprocesado y finalmente la obtención del gráfico.

La idea de esta estructura es debido a que se puede ejecutar el código a través de un IDE como Spyder o cualquier otro entorno que permita la lectura de ficheros planos de python **.py**

# Distribución del proyecto

En el proyecto se encunetran un total de 5 carpetas y dos ficheros *LICENSE* y *README*

- La primera carpeta se llama *Primera-tecnica*, dentro de ella se ecnontrará tanto el fichero de ejecución del gráfico como la carpeta *data* con el fichero csv de los datos obtenidos.

- La segunda carpeta se llama *Segunda-tecnica*, dentro de ella se ecnontrará nuevamente el fichero de ejecución del segundo gráfico y la carpeta *data* con los datos necesarios.

- La tercera carpeta se llama *tercera-tecnica*, en la que se ecnontrará el fichero de ejecución del tercer gráfico y la carpeta *data* con el último dataset obtenido para el proyecto.

- La cuarta carpeta se llama *Figuras*, en ella se encontrarán en formato **.png** las diferentes visualizaciones obtenidas.

-  La quinta carpeta se llama *Referencias*, en el que se situan todas las referencias empleadas a lo largo de la PEC.

Y finalmente los ficheros:

- LICENCIA, con la documentación obtenida de referencia

- README, con la infomación necesaria del proyecto

# Procedimiento para EJECUTAR LOS DIFERENTES CODIGOS

1- Descargar y descomprimir el proyecto

2- Abrir un IDE como *Spyder* que permita la ejecución de ficheros planos

3- Opcional (crear un entorno virtual para ejecutar el código mediante los comandos)

4- Instalar las tres librerías necesarias para la realización de los gráficos:

	pip install numpy
 	pip install pandas
  	pip install matplotlib.pyplot

5- Finalmente, ejecutar el código principal

**IMPORTANTE**

Si se usa el IDE *Spyder* recuerde modificar el path donde se encuentra el fichero de datos necesario para la creación del gráfico y es posible que se requiera de dos contrabarras para indicar un cambio de carpeta.
						*"c:\\Users\\mvinesr\\Escritorio\\Priemra_tecnica.csv"*


# OUTPUTS
**PRIMERA TÉCNICA**

- Tras ejecutar el primer codigo llamado *primera_tecnica.py*, se mostrará por el primer gráfico realizado el el cual se concoe como Pie Chart y en el que se muestra en porcentaje, el número de accidentes que han habido en Alcobendas en cada año desde 2020 hasta 2023. Es un gráfico simple peró extremadamente útil que permite observar como con el paso de los años, **existe un incremento en el número de accidentes de tráfico**.


![Primra técnica de visualización. **Pie CHart**](Figuras/Pie_chart.png)


- El segundo código llamado *segunda_tecnica.py*, permite mostrar en un stream plot la evolución en el tiempo de la administraciónd e dosis de vacunas contra la gripe administradas sobre distintas provincias de la región de Castilla y León. Esta visualización permite identificar patrones de vacunación como picos y disminuciones en el número de dosis administradas. En concreto el siguiente gráfico permitiría reflejar indirectamente la influencia que tuvo la pandemia por el COVID-19, epsecialmente en *2021* y en *2022*. Es possible que durante ese período de máximo apogeo del COVID, hubiese una mayor concienciación pública sobre la vacunación en general y en concreto de a  grípe. lo que supondría un incremento notable en las dosis administradas. 


![Primra técnica de visualización. **Pie CHart**](Figuras/Stream_plot.png)

- Por último, el código *tercera_tecnica.py*, permite mostrar en una visualización más avanzada, en concreto, se trata de un *Horizon graph*, el cual permite representar por contientes y en un períodod comprendido entre 2019 y 2023 el gasto edio de cada contiente. Este gráfico que tiene una cobertura temporal más amplia, permite ver nuevamente y de manera indirecta, la influncia que tuvo la pandemia sobre los diferentes contientes. Este gráfico que se establece mediante un gradiente de colores de diferentes intesidades, donde tonos azules indícan valores positivos y tonos rojos, valores negativos, permite ver como en el período de 2020 hasta finales de 2021, todos los contientes sufrieron un ingremento notable en los gástos medios.

![Primra técnica de visualización. **Pie CHart**](Figuras/Horizon_plot.png)


# Copyright, información de los datos y Licencias

- Copyright © 2001-2024 Python Software Foundation.

Consulte la LICENCIA para obtener información sobre el historial de este software.

Esta distribución de Python contiene código de Licencia Pública General (GPL) de GNU.

- Link de descarga de los datos (se encuentra de manera adicional en la Bibliografía):
  	- https://datos.gob.es/es/catalogo/l01280066-accidentes-de-trafico-en-alcobendas-desde-el-ano-2020
  	- https://datos.gob.es/es/catalogo/a07002862-vacunacion-frente-a-la-gripe-por-edad-sexo-y-provincia-campana-24-25
  	- https://datos.gob.es/es/catalogo/ea0010587-distribucion-del-gasto-turistico-y-gasto-medio-diario-realizado-segun-continente-de-destino-gdre-identificador-api-58709

- Licencias de las diferentes fuentes de datos obtenidas:

  	- http://www.opendefinition.org/licenses/odc-by
  	- https://www.ine.es/aviso_legal
  	- https://creativecommons.org/licenses/by/4.0/deed.es_ES
	
		 
		 
		 

