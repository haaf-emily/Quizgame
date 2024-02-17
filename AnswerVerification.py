import xmltodict
import random
from flask import Flask, jsonify, request
from flask_cors import CORS

# Schnittstelle Python/typescript
app = Flask(__name__)
CORS(app,supports_credentials=True)

# Schnittstelle Python/XMl-Datei
file = open("fragen.xml", encoding="utf-8")
xml_string = file.read()
python_dict = xmltodict.parse(xml_string)   # Umwandlung XML-Datei in Dictionary

question_key = None

# Zuweisung was ausgeführt werden soll bei HTTP-Request Get

@app.route('/api/questionOutput', methods=['GET'])
def questionOutput():

    message = 'Herzlich Willkommen zu Wer wird Informatiker?'   # Test auf Webseite das eine Verbindung da ist
    # Dynamische Variable für die von i ausgewählte Frage
    global question_key
    # Zufällige Auswahl der Fragen (aktuell gibt es 10 mögliche Fragen)
    i = random.sample(range(1, 11), 1)[0]
    
    
    # Fragen mit Antworten abrufen
    # Frage nach dem aktuellen Wert von i
    question_key = f'question{(i)}'
    # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
    if question_key in python_dict['questions']:
         questiontext= python_dict['questions'][question_key]['text']
    else:
        print(f'Fehler: Der Schlüssel {question_key} wurde nicht gefunden.')


    # Auswahl dynamischer Antworten über j 
    numberanswer = 0
    for j in random.sample(range(1, 5),4):
        # Frage nach dem aktuellen Wert von j
        answer_key = f'answer{(j)}'
        #Benötigt man für die Zuweisung für die Buttons
        numberanswer += 1
        
        # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
        if answer_key in python_dict['questions'][question_key]:
            # Ausgabe der Antworten und dient zur Antwortüberprüfung
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
    
    # Zuweisung der Wertübergabe
    data = {
            'message': message,
            'question': questiontext,
            'answer1': answer1,
            'answer2': answer2,
            'answer3': answer3,
            'answer4': answer4,
    }
    # Wertübergabe an Schnittstelle
    return jsonify(data)

# Zuweisung was ausgeführt werden soll bei HTTP-Request POST und OPTIONS
      
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

    # Variable correct für User, damit er sieht ob die Antwort richtig oder falsch ist
        
    print(python_dict['questions'][question_key]['answer4'])
    return jsonify(correct = f'{correct}')
    

# Zuweisung auf welchen Port Flask läuft  
if __name__ == '__main__':
    app.run(port=5000)