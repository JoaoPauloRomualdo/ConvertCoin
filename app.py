from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():    
    api_url ='https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(api_url)
    dados = response.json()
    
    # Extraindo as taxas de câmbio específicas
    name_usd_brl = dados['USDBRL']['name']
    usd_brl = round(float(dados['USDBRL']['bid']), 2)

    name_euro = dados['EURBRL']['name']
    eur_brl = round(float(dados['EURBRL']['bid']), 2)

    name_btc = dados['BTCBRL']['name'] 
    btc_brl = round(float(dados['BTCBRL']['bid']), 4)



    return render_template('convert.html',
                            usd_brl=usd_brl,
                            eur_brl=eur_brl,
                            btc_brl=btc_brl,
                            name_usd_brl = name_usd_brl,
                            name_euro = name_euro,
                            name_btc = name_btc
                            )

""" # Obtendo o valor digitado pelo usuário e convertendo para float
    user_input = float(request.form['user_input']) if 'user_input' in request.form else 0.0

    # Somando o valor digitado pelo usuário ao valor da moeda
    resultado_conversao = {
        'USD': usd_brl * user_input,
        'EUR': eur_brl * user_input,
        'BTC': btc_brl * user_input,
    }"""

if __name__ == "__main__" :
    app.run(debug=True)