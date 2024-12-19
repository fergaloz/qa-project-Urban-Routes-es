
![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtQhOxCbDgjJ74d_KCtNBNcje0EluubZntQQ&s)


# Proyecto Urban Routes

En este proyecto se automatizan las pruebas para comprobar la funcionalidad de **Urban Routes**.


## Contenido

* Servidor TT
* Configuración
* Pre requisitos
* Instalación
* Ejecutando las pruebas
* Pruebas

## Servidor TT

[URL servidor](https://cnt-a55375b7-709c-459d-a03c-83484eab58ad.containerhub.tripleten-services.com)





## Configuración

Para trabajar en este proyecto se debe clonar el repositorio de github o descargar el zip comprimido

## Pre requisitos

* PyCharm
* Conectividad al servidor TripleTen
* Cuenta github

### Paso 1: Conecta tu GitHub

El primer paso es enlazar tu cuenta de GitHub a TripleTen.
Esto te permitirá enviar tus proyectos automáticamente con tan solo hacer clic en un botón, directamente dentro de la plataforma de TripleTen.

### Paso 2: Clona el repositorio

Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será `qa-project-Urban-Routes-es`.

Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

  1. Abre la línea de comandos en tu computadora.
  2. Si aún no lo has hecho, crea un directorio para almacenar todos tus proyectos.
```bash
  cd ~             # asegúrate de estar en tu directorio de inicio
mkdir projects     # crea una carpeta llamada projects
cd projects        # cambia el directorio a la nueva carpeta de proyectos
```

3. Clona el repositorio con SSH.
```bash
git clone git@github.com:username/qa-project-Urban-Routes-es.git
```

```bash
   💡 Asegúrate de clonar el repositorio correcto. El nombre de usuario debe ser tu propio nombre de usuario, no tripleten-com.
```
## Instalación.
 ### Trabaja con el proyecto de forma local

Ahora tienes una copia local del proyecto y puedes abrir la carpeta del proyecto en tu computadora.

```bash
💡 Puedes utilizar PyCharm para trabajar en el proyecto localmente. Simplemente abre PyCharm y selecciona Archivo → Abrir y luego selecciona la carpeta qa-project-Urban-Routes-es que clonaste en tu computadora.
```
```bash
   Recuerda instalar pytest
```
Necesitaras estos archivos
* Data.py : Este archivo contiene la URL que necesitas y los datos necesarios para rellenar los campos que asi lo soliciten.
* Clase.py : Este archivo contiene los localizadores y la clase `UrbanRoutes`.
* Main.py : Archivo en el cual se encuentra la clase `TestUrbanRoutes` y las pruebas de funcionalidad.

Cuando puedas comenzar a trabajar, "Inicia el servidor" para obtener la URL de tu servidor.



## Ejecutando las pruebas

Para poder correr las pruebas es necesario actualizar la url del servidor en el archivo Data.

```bash
  URL_SERVICE = " https://cnt-0ed52d02-902a-4915-bf36-38a9c84d15dc.containerhub.tripleten-services.com?lng=es"
```

Para poder realizar la comprobación de las pruebas de funcionalidad de `Urban Routes` es necesario contar con lo siguiente:

```bash
 1.- Archivo Data.
 2.- Localizadores y métodos en la clase UrbanRoutesPage .
 3.- Pruebas para la funcionalidad en la clase TestUrbanRoutes.

 💡
```

## Pruebas

| N° | Descripción    | l
| :-------- | :------- | :------------------------- |
| 1 | 	Configurar la dirección.
| 2 | 	Seleccionar la tarifa Comfort.
| 3 | Rellenar el número de teléfono.
| 4 | 	Agregar una tarjeta de crédito.
| 5 | 	Escribir un mensaje para el conductor.
| 6 | 	Pedir una manta y pañuelos.
| 7 | 	Pedir 2 helados.
| 8 | 	Aparece el modal para buscar un taxi.



