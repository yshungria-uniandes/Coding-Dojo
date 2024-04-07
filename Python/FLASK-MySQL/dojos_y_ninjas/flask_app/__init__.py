# Importación de Flask
from flask import Flask

# Creación de la instancia de la aplicación o inicialización de la aplicación
app = Flask(__name__)

# Configuración de la clave secreta
app.secret_key = "secret"