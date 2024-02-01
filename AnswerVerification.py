import xmltodict
import random

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
    """ respons_key = f'question{(user_input)}'

    # Überprüfen, ob die Nutzereingabe mit den erwarteten Antworten übereinstimmt
    if python_dict['questions'][question_key][respons_key] == masteranswer:
        print("Richtig! Die Antworten sind korrekt.")
    else:
        print("Falsch! Die Antworten sind nicht korrekt.") """

print("Hallo zum Quizgame: Wer wird Informatiker?")
masteranswer= questionOutput(i=1)
responseCheck(masteranswer)
file.close()