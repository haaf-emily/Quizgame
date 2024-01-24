import xmltodict

employee={'employee': {'name': 'John Doe', 
                       'age': '35', 
                       'job': {'title': 'Software Engineer', 'department': 'IT', 'years_of_experience': '10'}, 
                       'address': {'street': '123 Main St.', 'city': 'San Francisco', 'state': 'CA', 'zip': '94102'}, 
                       }}
file=open("employee.xml","w")
xml_string=xmltodict.unparse(employee)
file.write(xml_string)
file.close()