# Vangoghstagram
=======

Instalación
===========

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
$ sudo apt-get install python-pip
```

## instalacion del entorno virtual con virtuelenv
```bash
$ sudo apt-get install python-virtualenv
````

## Creacion y Activacion del entorno virtual con virtualenv ( python3 )
```bash
$ virtualenv -p python3 myvenv
$ source myvenv/bin/activate
````
## Instalacion del entorno virtual con virtualenvwripper
```bash
$ sudo apt-get install -y virtualenvwrapper
```

## Agregar estas lineas en ~/.zshrc o ~/.bashrc
```bash
$ export WORKON_HOME=$HOME/.virtualenvs
$ source /usr/local/bin/virtualenvwrapper.sh
```

## Cargar de nuevo zshrc o bashrc
```bash
$ source ~/.zshrc o ~/.bashrc 
```

## Crear el entorno virtual y Activacion
```bash
$ mkvirtualenv myvenv
$ WORKON myvenv
```

## Clonar el proyecto
```bash
$ git clone https://github.com/LopsanAMO/Vangoghstagram.git
$ cd zastask
```

# Instalación de las dependencias
```bash
$ pip install psycopg2
$ pip install -r requerimientos.txt
```

# Ejecutar el proyecto
```bash
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8000
