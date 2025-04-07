from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    if isinstance(target_currency, list):
        target_currency = ','.join(target_currency)

    cf = fetch_conversion_factor(source_currency, target_currency)
    final_amount = amount * cf

    response = {
        'fulfillmentText': f"{amount} {source_currency} is {final_amount:.2f} {target_currency}"
    }
    return jsonify(response)

def fetch_conversion_factor(source, target):
    url = f"https://apilayer.net/api/live?access_key=07a01508aac6b86e8427d073ffff616e&currencies={target}&source={source}&format=1"
    response = requests.get(url)
    data = response.json()

    key = f"{source}{target}"
    return data["quotes"][key]

if __name__ == "__main__":
    app.run(debug=True)
