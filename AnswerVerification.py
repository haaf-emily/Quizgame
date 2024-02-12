import xmltodict
import random
from flask import Flask, jsonify, request
from flask_cors import CORS

#Schnittstelle Python/typescript
app = Flask(__name__)
CORS(app,supports_credentials=True)
# Einlesen von der XML Datei
file = open("fragen.xml", encoding="utf-8")
xml_string = file.read()
python_dict = xmltodict.parse(xml_string)

question_key = None


@app.route('/api/questionOutput', methods=['GET'])
def questionOutput():
    #i = 5

    message = 'Herzlich Willkommen zu Wer wird Informatiker?'   # Test auf Webseite das eine Verbindung da ist
    global question_key
    i = random.sample(range(1, 11), 1)[0]
    
    
    # Fragen mit Antworten abrufen
    # Frage nach dem aktuellen Wert von i
    question_key = f'question{(i)}'
    # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
    if question_key in python_dict['questions']:
         #print(python_dict['questions'][question_key]['text'])
         questiontext= python_dict['questions'][question_key]['text']
         #return jsonify(question = questiontext)
    else:
        print(f'Fehler: Der Schlüssel {question_key} wurde nicht gefunden.')


    # Dynamische Antworten durchlaufen
    numberanswer = 0
    for j in random.sample(range(1, 5),4):
        # Frage nach dem aktuellen Wert von i
        answer_key = f'answer{(j)}'
        numberanswer += 1
        
        # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
        if answer_key in python_dict['questions'][question_key]:
            # Ausgabe der Antworten und dient zur Antwortüberprüfung
            #print(f"{numberanswer} {python_dict['questions'][question_key][answer_key]}" )
            #answer = python_dict['questions'][question_key][answer_key]

            # Ausgabe der Antworten
            if numberanswer==1:
                answer1=python_dict['questions'][question_key][answer_key]
            elif numberanswer==2:
                answer2=python_dict['questions'][question_key][answer_key]
            elif numberanswer==3:
                answer3=python_dict['questions'][question_key][answer_key]
            else:
                answer4=python_dict['questions'][question_key][answer_key]
        else:
            print(f'Fehler: Der Schlüssel {answer_key} wurde nicht gefunden.')
    
    data = {
            'message': message,
            'question': questiontext,
            'answer1': answer1,
            'answer2': answer2,
            'answer3': answer3,
            'answer4': answer4,
    }
    return jsonify(data)
      
@app.route('/api/responseCheck', methods=['POST', 'OPTIONS'])
def responseCheck():
    if request.method == 'OPTIONS':
        # Antwort auf OPTIONS-Anfrage ohne Daten
    
        return ' ', 204


    data = request.json  # Zugriff auf die JSON-Daten der Anfrage
    print('Received data:', data)
    


    
    # Nur den Wert ("answer") ausgeben
    answer = data.get('selectedAnswer', None)   
    answer= f'{answer}'
    answer = answer.lstrip()  # Leerzeichen am Anfang wird entfernt

    # Antwortüberprüfung
    if answer==python_dict['questions'][question_key]['answer4']:
        correct="Richtig"
    else:
        correct="Falsch"

    print('Value:', answer)    #   Ausgabe in Terminal Value: {'ant1': ' Reelle Zahlen'}
    print(python_dict['questions'][question_key]['answer4'])
    return jsonify(correct = f'{correct}')
    

  

#questionOutput(1)
if __name__ == '__main__':
    app.run(port=5000)

