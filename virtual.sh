#!/bin/bash

# python3 -m venv virtual
# . virtual/bin/activate

py -3 -m venv virtual
virtual\\Scripts\\activate

pip install -U pip
pip install Flask python-dateutil

pip install flask-sqlalchemy mysqlclient
pip install flask-bcrypt
pip install flask-login

