# Documentación Django 2
# Documentación Django 2
Se requiere de Python en su versión 3.6.8

## Instalación de paquetes requeridos
### Python Pip
Para instalar el gestor de paquetes de python:
```
sudo apt-get install python3-pip
```

### Entorno Virtual
Instalación
```
sudo apt-get install python3-venv
```
Creación
```
python3.6 -m venv nombreDelVenv
```
Activación del entorno virtual: ```source nombreDelVencv/bin/activate```

Una vez activado el entorno virtual verificar que la versión de python predeterminada sea la 3.6: ```python --version```

### Instalación de Django
Para instalar una version especifica:
```
pip install django==2.2
```

## Creación del Proyecto en Django
Se recomienda crear una carpeta con el nombre del proyecto con la primera letra en mayúscula, luego ingresamos a ella en la terminal.
```
django-admin startproject nombreProyecto
```
***Nota:*** El nombre del proyecto debe iniciar con letra minúscula.
