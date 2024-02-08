from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello from Python!')


@app.route('/api/process_data', methods=['POST', 'OPTIONS'])
def process_data():
    if request.method == 'OPTIONS':
        # Antwort auf OPTIONS-Anfrage ohne Daten
    
        return 'x', 204


    data = request.json  # Zugriff auf die JSON-Daten der Anfrage
    print('Received data:', data)
    

    # Lösungen von ChatGpt
    
    # Nur den Wert ("value") ausgeben
    value = data.get('key', None)
    
    print('Value:', value)
    
    
    # Hier kannst du die übermittelten Daten weiterverarbeiten

    #return jsonify(result='Data processed successfully')
    if value is not None:
        print('Value:', value)
        result=f'Data processed successfully. Received value: {value}'
        value = f'{value}'
        response_data = {
            'result': result,
            'answer': value
        }
        
        return jsonify(response_data) 
    else:
        print('No value found in received data')
        return jsonify(error='No value found in the received data'), 400

if __name__ == '__main__':
    app.run(port=5000)
