Venezuela
=========

Es un proyecto desarrollado con Django 1.6 (con a tag de Django 1.5).

El proyecto en su fase inicial es para tener la base de datos de Estados, Municipio y parroquias de venezuela


Sobre la base de datos
======================

Inicialmente la base de datos fue recopilada por José A. Rodriguez E. publicada en su blog:

* http://josearodrigueze.wordpress.com/2013/04/23/bd-pais-estado-municipio-parroquia/

Luego la base de datos fue importada al formato json para que pueda ser utilizada con Django desde cualquier base de datos.


Para ejecutar el proyecto con virtual env
=========================================

Virtualenv
----------

Asegurate de tener instalado virtualenv (http://www.virtualenv.org). Si ya lo tienes instalado ejecuta::

    $ virtualenv venv_venezuela

Luego

Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django


Clona el proyecto
=================

To create a new Django project called '**icecream**' using
django-twoscoops-project, run the following command::

    $ git clone https://github.com/hernanramirez/venezuela.git


Instala las dependencias
========================

Depending on where you are installing dependencies:

Para desarrollo::

    $ pip install -r requirements/local.txt

Para producción::

    $ pip install -r requirements.txt

Por hacer
=========

.. image:: http://laprimeraplana.com.mx/wp-content/uploads/2013/04/10-cosas-por-hacer-cada-d%C3%ADa-de-trabajo.jpg
   :name: Por hacer
   :align: center
   :alt: Por hacer
   :target: http://laprimeraplana.com.mx

Tengo en mente hacer la base de datos de Venezuela con `Banderas, escudos y mapa`_.

.. _`Java Script`: De autocompletado estado, municipio y parroquia
.. _`Banderas y escudos`: completar cada estado, municipio y parroquia con banderas y escudos
.. _`Generar con geodjango mapas`: completar cada estado, municipio y parroquia mapas

