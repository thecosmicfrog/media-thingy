#!/bin/bash

rm music/__init__.pyc
mv music/__init__.py music/__init_temp__.py
touch music/__init__.py

rm picture/__init__.pyc
mv picture/__init__.py picture/__init_temp__.py
touch picture/__init__.py

rm video/__init__.pyc
mv video/__init__.py video/__init_temp__.py
touch video/__init__.py

python manage.py syncdb

rm music/__init__.py*
rm picture/__init__.py*
rm video/__init__.py*

mv music/__init_temp__.py music/__init__.py
mv picture/__init_temp__.py picture/__init__.py
mv video/__init_temp__.py video/__init__.py
