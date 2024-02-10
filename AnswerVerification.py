import xmltodict
import random
from flask import Flask, jsonify, request
from flask_cors import CORS

#Schnittstelle Python/typescript
app = Flask(__name__)
CORS(app,supports_credentials=True)

file = open("fragen.xml", encoding="utf-8")
xml_string = file.read()
python_dict = xmltodict.parse(xml_string)

question_key = None


@app.route('/api/questionOutput', methods=['GET'])
def questionOutput():
    i = 1
    global question_key
    #data = request.json  # Zugriff auf die JSON-Daten der Anfrage
    message = 'Herzlich Willkommen zu Wer wird Informatiker?'
    #return jsonify(message= 'Hello')
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
            #'answer': answer,
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
    

    # Lösungen von ChatGpt
    
    # Nur den Wert ("value") ausgeben
    answer = data.get('selectedAnswer', None)   # Name answer kannst du ändern
    answer= f'{answer}'
    print('Value:', answer)    #   Ausgabe in Terminal Value: {'ant1': ' Reelle Zahlen'}
    
    return jsonify(result='Data processed successfully')
    
    # Hier kannst du die übermittelten Daten weiterverarbeiten

    
    
    
    
    
    """ #return jsonify(result='Data processed successfully')
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
        return jsonify(error='No value found in the received data'), 400  """

#questionOutput(1)
if __name__ == '__main__':
    app.run(port=5000)






""" @app.route('/api/get_question', methods=['GET'])
def get_question():
    i = request.args.get('i', type=int)
    return jsonify({'question': questionOutput(i)})

@app.route('/api/check_response', methods=['POST'])
def check_response():
    user_input = request.json['user_input']
    masteranswer = request.json['masteranswer']
    return jsonify({'result': responseCheck(user_input, masteranswer)})

def questionOutput(i):
    global question_key
    # Annahme: Der Wert von i sollte eine gültige Frage repräsentieren
    question_key = f'question{(i)}'
    if question_key in python_dict['questions']:
        return python_dict['questions'][question_key]
    else:
        return {'error': f'Der Schlüssel {question_key} wurde nicht gefunden.'}

def responseCheck(user_input, masteranswer):
    respons_key = f'answer{(user_input)}'
    # Überprüfen, ob die Nutzereingabe mit den erwarteten Antworten übereinstimmt
    if respons_key in masteranswer and masteranswer[respons_key] == True:
        return "Richtig! Die Antwort ist korrekt."
    else:
        return "Falsch! Die Antwort ist nicht korrekt." """



""" 
# Von Emily 
import xmltodict
import random
from flask import Flask, jsonify, request
from flask_cors import CORS

#Schnittstelle Python/typescript
app = Flask(__name__)
CORS(app,supports_credentials=True)

file = open("fragen.xml", encoding="utf-8")
xml_string = file.read()
python_dict = xmltodict.parse(xml_string)

question_key = None

def questionOutput(i):
    global question_key
    # Fragen mit Antworten abrufen
    # Frage nach dem aktuellen Wert von i
    question_key = f'question{(i)}'
    # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
    if question_key in python_dict['questions']:
         print(python_dict['questions'][question_key]['text'])
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
            print(f"{numberanswer} {python_dict['questions'][question_key][answer_key]}" )
            
        else:
            print(f'Fehler: Der Schlüssel {answer_key} wurde nicht gefunden.')


def responseCheck(masteranswer):
    user_input = input("Bitte geben Sie von Ihre Antwort die Zahlen ein: ")
    respons_key = f'question{(user_input)}'

    # Überprüfen, ob die Nutzereingabe mit den erwarteten Antworten übereinstimmt
    if python_dict['questions'][question_key][respons_key] == masteranswer:
        print("Richtig! Die Antworten sind korrekt.")
    else:
        print("Falsch! Die Antworten sind nicht korrekt.") 

print("Hallo zum Quizgame: Wer wird Informatiker?")
masteranswer= questionOutput(i=1)
responseCheck(masteranswer)
file.close() 

#Schnittstelle Python/typescript
if __name__ == '__main__':
    app.run(port=5000)
 """

""" import xmltodict
import random

def load_questions(filename="fragen.xml"):
    with open(filename, encoding="utf-8") as file:
        xml_string = file.read()
    return xmltodict.parse(xml_string)

def get_question_key(index):
    return f'question{index}'

def display_question(question_key, questions_dict):
    question_data = questions_dict.get('questions', {}).get(question_key, {})
    if question_data:
        print(question_data.get('text', 'Fehler: Text nicht gefunden.'))
    else:
        print(f'Fehler: Der Schlüssel {question_key} wurde nicht gefunden.')

def get_random_answers(question_key, questions_dict):
    answer_options = []
    for j in random.sample(range(1, 5), 4):
        answer_key = f'answer{j}'
        answer_data = questions_dict.get('questions', {}).get(question_key, {}).get(answer_key)
        if answer_data:
            answer_options.append(answer_data)
            print(f"{len(answer_options)} {answer_data}")
    return answer_options

def question_output(index, questions_dict):
    question_key = get_question_key(index)
    display_question(question_key, questions_dict)
    return get_random_answers(question_key, questions_dict)

def response_check(master_answer, user_input, next_question_index, questions_dict):
    if user_input == master_answer:
        print("Richtig! Die Antwort ist korrekt.")
    else:
        print("Falsch! Die Antwort ist nicht korrekt.")
    question_output(next_question_index, questions_dict)

def main():
    questions_dict = load_questions()
    print("Hallo zum Quizgame: Wer wird Informatiker?")
    index = 1
    master_answer = question_output(index, questions_dict)
    user_input = input("Bitte geben Sie Ihre Antwort als Zahl ein: ")
    next_question_index = index + 1
    response_check(master_answer, user_input, next_question_index, questions_dict)

if __name__ == "__main__":
    main()
 """