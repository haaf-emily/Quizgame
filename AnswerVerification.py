import  testFragen
import xml.etree.ElementTree as ET
class answerverification:

    def parse_xml(testFragen):
        tree = ET.parse(testFragen)
        root = tree.getroot()
        
        questions = []
        
        for question_elem in root.findall('question'):
            text = question_elem.find('text').text
            answers = [answer.text for answer in question_elem.findall('answer1')]
            
            question = {'text': text, 'answers': answers}
            questions.append(question)
        
        return questions

    if __name__ == "__main__":
        file_path = "testFragen.xml"
        questions = parse_xml(file_path)
        
        for i, question in enumerate(questions, 1):
            print(f"\nFrage {i}: {question['text']}")
            print("Antworten:")
            for answer in question['answers']:
                print(f"  - {answer}")

    from testFagen.xml import parse_xml

    file_path = "deine_xml_datei.xml"
    questions = parse_xml(file_path)

    for i, question in enumerate(questions, 1):
        print(f"\nFrage {i}: {question['text']}")
        print("Antworten:")
        for answer in question['answers']:
            print(f"  - {answer}")