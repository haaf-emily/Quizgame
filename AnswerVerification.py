import xmltodict
import random

file = open("fragen.xml", encoding="utf-8")
xml_string = file.read()
python_dict = xmltodict.parse(xml_string)


def questionOutput(i):
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
        numberanswer = numberanswer + 1
        
        # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
        if answer_key in python_dict['questions'][question_key]:
            # Ausgabe der Antworten und dient zur Antwortüberprüfung
            if j==1:
                print(f"{numberanswer} {python_dict['questions'][question_key][answer_key]}" )
            elif j==2:
                print(f"{numberanswer} {python_dict['questions'][question_key][answer_key]}" )
            elif j==3:
                print(f"{numberanswer} {python_dict['questions'][question_key][answer_key]}")
            else:
                print(f"{numberanswer} {python_dict['questions'][question_key][answer_key]}" )
        else:
            print(f'Fehler: Der Schlüssel {answer_key} wurde nicht gefunden.')


def responseCheck():
    print("Hi")

print("Hallo zum Quizgame: Wer wird Informatiker?")
questionOutput(i=1)
print('Bitte gebe o')
responseCheck()
file.close()