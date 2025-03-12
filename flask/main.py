from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_address', methods=['POST'])
def get_address():
    cep = request.form['cep']
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if response.ok:
        return response.json()
    return {'error': 'CEP não encontrado'}, 404


if __name__ == '__main__':
    app.run(debug=True)
