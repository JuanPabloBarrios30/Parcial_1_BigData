<p align = center  
<br>
<img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png" align="center"><br><FONT FACE="times new roman" SIZE=6>
<b>Parcial #1: Big Data</b>
<br>
<i><b>Autores:</b></i> Juan Pablo Barrios Suarez y Paula Sofía Godoy Salamanca
<br>
<i><b>Semestre:</b></i> 9º
<br>
<i><b>Asignatura:</b></i> Big Data
<br>
<i><b>Docente:</b></i> Camilo Rodríguez
<br>
<i><b>Fecha: </b>12/03/2022
<br>
<b>Ciencias de la computación e inteligencia artificial</b></i>
<br>
</FONT>
</p>


# **Parte 1**
- Usando zappa crear una función lambda que descargue la primera página de resultados del sitio Finca Raiz(https://www.fincaraiz.com.co) para la venta de casas en el sector de chapinero.
Esta lambda se debe ejecutar todos los lunes a las 9 am.
La página html se debe guardar en un bucket s3://landing-casas-xxx/yyyy-mm-dd.html

## **Implementación**

Para la ejecución de este proyecto, se deben ingresar los siguientes comandos en la terminal:
- Ingresar a la carpeta
```
cd lambda_uno
```
- Crear el entorno y activarlo
```
pip install virtualenv
virtualenv -p python3.8 env
source env/bin/activate
```
- Instalar las bibliotecas necesarias
```
pip install -r requirements.txt
```
- Ejecutar el archivo `apps.py`
```
zappa update dev
zappa invoke apps.f
```


# **Parte 2**
- Al llegar la página web al bucket se debe disparar un segundo lambda que procese el archivo utilizando el paquete de python beatifulsoup y extraiga la información de cada casa.
Se debe crear un archivo CSV en s3://casas-final-xxx/yyyy-mm-dd.csv con la siguiente estructura de columnas:
FechaDescarga, Barrio, Valor, NumHabitaciones, NumBanos, mts2

## **Implementación**

Para la ejecución de este proyecto, se deben ingresar los siguientes comandos en la terminal:
- Ingresar a la carpeta
```
cd lambda_2
```
- Crear el entorno y activarlo
```
pip install virtualenv
virtualenv -p python3.8 env
source env/bin/activate
```
- Instalar las bibliotecas necesarias
```
pip install -r requirements.txt
```
- Ejecutar el archivo `apps.py`
```
zappa update dev
zappa invoke apps.lambda_handler
```

# **Parte 3**
- Se deben utilizar pruebas unitarias con pytest(mínimo 3). Para probar la función de descarga utilizar un mock(https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python)

## **Implementación**

Para la ejecución de las pruebas unitarias, se deben ingresar los siguientes comandos en la terminal:
- Ingresar a la carpeta
```
cd lambda_uno
```
- Activar el entorno
```
source env/bin/activate
```
- Ejecutar el siguiente comando
```
pytest
```

# **Parte 4**
- Se debe crear un pipeline de despliegue continuo con GitHubActions al hacer push o pull request con las siguientes etapas:

> 1. Revisión de código limpio con flake8

> 2. Ejecución de pruebas unitarias

> 3. Despliegue automático en AWS

## **Implementación**

Para verificar el Pipeline de despliegue, abra el archivo `workflow.yml` que se encuentra en la carpeta `.github/workflows`


> **Nota:** Se deben haber configurado las credenciales de AWS con el repositorio para el correcto funcionamiento del Pipeline de despliegue.
