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

5- Finalmente, ejecutar el código principal *main.py* mediante el comando:

	python3 main.py

# Procedimiento para ejecutar los tests y la cobertura

Existen un total de 6 test, uno por cada ejercicio. Estos se ejecutan de la siguiente manera:

	python3 -m unittest test_1.py (para el primer test)

	python3 -m unittest test_2.py (para el segundo test)

	python3 -m unittest test_3.py (para el tercer test)

	python3 -m unittest test_4.py (para el tercer test)
	
	python3 -m unittest test_5.py (para el tercer test)
	
	python3 -m unittest test_6.py (para el tercer test)

Adicionalmente, para ver los porcentajes de cobertura de cada test se emplea el comando

	coverage run -m pytest -v

# OUTPUTS

Tras ejecutar el primer codigo llamado *primera_tecnica.py*, se mostrará por el primer gráfico realizado el el cual se concoe como Pie Chart adjuntado a continuación


![Primra técnica de visualización. **Pie CHart**](Figuras/Pie_chart.png)


- ejercicio4_1.png (Con la distribución de las variables permit, handgun y long_gun a lo largo de los años)
- Los diferentes mapas en formato .html y en formato PNG

# Copyright y información de Licencias

- Copyright © 2001-2024 Python Software Foundation.

Consulte la LICENCIA para obtener información sobre el historial de este software.

Esta distribución de Python contiene código de Licencia Pública General (GPL) de GNU.
	
		 
		 
		 

