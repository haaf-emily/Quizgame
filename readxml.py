import xmltodict
file=open("TestQuestion.xml","r")
xml_string=file.read()
print(xml_string)
python_dict=xmltodict.parse(xml_string)
print(python_dict)
file.close()