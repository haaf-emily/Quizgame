import xmltodict
file=open("Testfrage.xml","r")
xml_string=file.read()
#print("The XML string is:")              #nur zum überprüfen nötig
#print(xml_string)                        #nur zum überprüfen nötig
python_dict=xmltodict.parse(xml_string)

print(python_dict['question']['text'])
print(python_dict['question']['request1'])           #Antwort 4 immer richtig

#print("The dictionary created from XML is:")
#print(python_dict)
file.close()