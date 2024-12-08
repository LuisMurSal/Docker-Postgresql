#!/bin/bash

# Iniciar Nginx
service nginx start

# Iniciar la aplicación Flask
python3 /app/app.py
