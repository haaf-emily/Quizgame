import xmltodict

def dynamicQuestion(i):
    return i
def dynamicAnswer(j):
    j=j+1
    return j

file = open("fragen.xml", encoding="utf-8")
xml_string = file.read()
python_dict = xmltodict.parse(xml_string)


def keys():
    # Fragen mit Antworten abrufen
    for i in range(10):
        # Frage nach dem aktuellen Wert von i
        question_key = f'question{dynamicQuestion(i)}'
        
        # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
        if question_key in python_dict['questions']:
            print(python_dict['questions'][question_key]['text'])
        else:
            print(f'Fehler: Der Schlüssel {question_key} wurde nicht gefunden.')
    # Dynamische Antworten durchlaufen
        for j in range(4):
            # Frage nach dem aktuellen Wert von i
            answer_key = f'answer{dynamicAnswer(j)}'
            
            # Überprüfen, ob der Schlüssel im Dictionary vorhanden ist
            if answer_key in python_dict['questions']:
                print(python_dict['questions'][question_key][answer_key])
            else:
                print(f'Fehler: Der Schlüssel {answer_key} wurde nicht gefunden.')


print("Hallo zum Quizgame: Wer wird Informatiker?")
keys()
file.close()