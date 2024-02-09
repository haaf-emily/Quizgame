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
            if j==5:
                return python_dict['questions'][question_key][answer_key]
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