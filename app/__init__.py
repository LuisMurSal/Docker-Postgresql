from flask import Flask

app = Flask(__name__)

# Importar las rutas y otros módulos después de la creación de la app
from app import routes
