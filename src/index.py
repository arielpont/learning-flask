from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

# Permite que la app siga escuchando y se pueda ejecutar.
# Debug = True permite evitar tener que ejecutar index.py cada ves que hacemos un cambio para verlo reflejado.
if __name__ == '__main__':
	app.run(debug = True)