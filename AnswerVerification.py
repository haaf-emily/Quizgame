""" import xml.etree.ElementTree as ET
import xmltodict

# Öffnen Sie die XML-Datei
with open("testFragen.xml") as file:
    xml_string = file.read()

# Konvertieren Sie XML in ein Python-Dictionary
python_dict = xmltodict.parse(xml_string)

# Iterieren Sie über die Fragen und drucken Sie den Text jeder Frage
questions = python_dict['questions']['question']
for question in questions:
    print("Frage:", question['text'])

# Drucken Sie den allgemeinen Text des Quizgames
print("Quizgame: Wer wird Informatiker?")
print(python_dict['questions']['text']) """

import xml.etree.ElementTree as ET
import xmltodict
import test

file=open("testFragen.xml")
xml_string=file.read()
python_dict=xmltodict.parse(xml_string)
print(python_dict['questions']['question'])
file.close()
    
print("Quizgame: Wer wird Informatiker?")
print(python_dict['text'])
