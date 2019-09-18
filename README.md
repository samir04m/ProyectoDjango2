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

### Creación de una Aplicación
En la carpeta raíz del proyecto creamos una carpeta llamada “apps” nos posicionamos dentro de ella en la terminal y colocamos
```
django-admin startapp nombreAplicacion
```
Dentro de la carpeta apps se crea un archivo llamado  __ _init_ __.py

Recordar que cada aplicación que se cree se debe incluir en la lista ***INSTALLED_APPS*** en archivo ***settings.py***

### Creación de Modelos y Migración
Luego de crear los modelos, se configura la base de datos a utilizar.

Para crear y migrar:
```
 python manage.py makemigrations
```
```
 python manage.py migrate

```
Creación de un super usuario
```
python manage.py createsuperuser
```

### Relaciones en Modelos
Uno a uno: ```autor_id = models.OneToOneField(Autor, on_delete=models.CASCADE)```

Uno a muchos: ```autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)```

Muchos a muchos: ```autor_id = models.ManyToManyField(Autor)```

## Plugins
[Django Import Export](https://django-import-export.readthedocs.io/en/latest/installation.html)

[Django CKEditor](https://django-ckeditor.readthedocs.io/en/latest/#installation)

## Query sets
Busquedas exactas (Importa Mayus y minus): ```modelo = Modelo.objects.get(campo__exact = 'valor')```
Busquedas inexactas (No Importa Mayus y minus): ```modelo = Modelo.objects.get(campo__iexact = 'valor')```
Si esta contenido en una palabra: ```modelo = Modelo.objects.get(campo__icontains = 'valor')```

**Para filtar por el valor de un atributo del modelo de la relacion**

```modelo = Modelo.objects.filter(otroModelo__campo = 'valor')```

## Templates
**Imprimir el Label de un campo Tipo** ```{{  objeto.get_tipo_display }}```

**Modificar impresion un DateFielda o DateTimeField** ```{{  objeto.fecha|date:'H:i d-m-Y' }}```
[Mas Información](https://simpleisbetterthancomplex.com/references/2016/06/21/date-filter.html)

**Truncar o limitar numero de caracteres**  ``` {{object.texto|truncatechars:'10'}} ```

