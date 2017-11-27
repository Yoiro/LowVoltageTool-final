from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Bienvenue dans l\'Outil Basse Tension!'

if __name__ == '__main__':
    app.run(debug=True)