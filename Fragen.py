import xmltodict
file=open("fragen.xml","r")
xml_string=file.read()
#print("The XML string is:")              #nur zum überprüfen nötig
#print(xml_string)                        #nur zum überprüfen nötig
python_dict=xmltodict.parse(xml_string)

print(python_dict['questions']['question1']['text'])
print(python_dict['questions']['question1']['answer1'])           #Antwort 4 immer richtig

#print("The dictionary created from XML is:")        #nur zum überprüfen nötig
#print(python_dict)                                   #nur zum überprüfen nötig
file.close()