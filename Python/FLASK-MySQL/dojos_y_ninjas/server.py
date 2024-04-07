#Importacion de app
from flask_app import app

#Importacion de controladores
from flask_app.controllers import dojos, ninjas

#Ejecucion de la aplicacion
if __name__=="__main__":   
    app.run(debug=True) 