import xmltodict
file=open("employee.xml","r")
xml_string=file.read()
print("The XML string is:")
print(xml_string)
python_dict=xmltodict.parse(xml_string)
print("The dictionary created from XML is:")
print(python_dict)
file.close()