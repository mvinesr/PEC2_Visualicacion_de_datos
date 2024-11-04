# PEC2_Visualicacion_de_datos
Repositorio para publicar los diferentes resultados obtenidos a través del análisis de los tres datasets analizados para esta PEC.

La siguiente práctica se basa en la creación de diferentes codigos de Python con el fin de represetnar tres técnicas específicas de visualizaciónd e datos:

De este modo, el objetivo de esta práctica consta en desarrollar un conjunto de scripts de Python, que permita resolver diferentes cuestiones que se irán abordando. Para la realización
del código que se organiza de manera lógica separando por diferentes archivos planos .py por ejercicios de tal modo que existen un total de **3 archivos planos**

- Primera_tecnica.py

- Segunda_tecnica.py

- Tercera_tecnica.py

Cada uno de estos archivos planos consta de diferentes líneas de codigo que permiten analizar el conjunto de datos, hacer una primera base de preprocesado y finalmente la obtención del gráfico.

La idea de esta estructura es debido a que puedes ejecutar cada código por separado situándote dentro de la ubicación dónde se encuentran los diferentes archivos y así poder ejecutar el código por separado mediante el comando:

	**python3 Ejercicio_1.py**

# Distribución de los archivos

En el ZIP se encuentran diferentes carpetas:

- Data (con los dos archivos necesarios para ejecutar los diferentes archivos planos)

- Figuras (con las figuras que se han obtenido de los ejercicios)

- **Los diferentes archivos planos (.py), con todo el código**

- Referencias (Documento con todas las referencias empleadas a lo largo de la PEC))

- LICENCIA (Documentación obtenida de referencia [8])

- requierements.txt (con la información de las librerías básicas utilizadas)

# Procedimiento para EJECUTAR LOS DIFERENTES CODIGOS

1- Descargar y descomprimir la carpeta comprimida con toda la información (VinesManuel_PEC4.zip)

2- Mediante comandos cd, situarse dentro de la carpeta *VinesManuel_PEC4*

3- Opcional (crear un entorno virtual para ejecutar el código mediante los comandos):

	virtualenv venv
	source venv/bin/activate

4- Instalar todas las librerías que se encuentran dentro del fichero *requirements.txt* mediante el comando:

	pip install -r requirements.txt

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

Tras ejecutar el código, se mostrará por el terminal el resultado de todas las funciones, se abrirán los mapas en el buscador
y se obtendrán los siguientes archivos:

- ejercicio4_1.png (Con la distribución de las variables permit, handgun y long_gun a lo largo de los años)
- Los diferentes mapas en formato .html y en formato PNG

# Copyright y información de Licencias

- Copyright © 2001-2024 Python Software Foundation.

Consulte la LICENCIA para obtener información sobre el historial de este software.

Esta distribución de Python contiene código de Licencia Pública General (GPL) de GNU.
	
		 
		 
		 

