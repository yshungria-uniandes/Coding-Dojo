from flask import Flask

app = Flask(__name__)
app.secret = 'secret_key'