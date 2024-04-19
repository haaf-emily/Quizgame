# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

<u>Gruppenmitglieder</u>: 
Emily Haaf, Alexandra Altun  & Theresia Deubert

Unser **Git Account** für das Projekt: https://github.com/haaf-emily/Quizgame 

Zur vereinfachten Abbildung und Beweisführung der verwenden Codebestandteile Beziehen sich alle Aussagen ohne separate Abbildungen auf die Folgenden Bilder:

![Pasted image 20240225143325](https://github.com/haaf-emily/Quizgame/assets/152873694/95cf4c9c-29af-4c0e-b3a3-5cd56c2a571b)


![[Pasted image 20240225143337.png]]
![Pasted image 20240225143337](https://github.com/haaf-emily/Quizgame/assets/152873694/92419f3e-397e-43c3-8003-21e292550526)

![[Pasted image 20240225143406.png]]
![Pasted image 20240225143406](https://github.com/haaf-emily/Quizgame/assets/152873694/d3195ad2-d0be-49ac-bdef-df4192de4ba1)


## FACHKOMPETENZ (40 Punkte)

### Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

#### Algorithmenbeschreibung
Wir können Algorithmen beschreiben und sie detailliert erklären. Dies kann man an unseren Kommentare im Code nachvollziehen.

#### Datentypen
In unseren Projekt haben wir  verschieden Datentypen verwendet. Die einzelnen Datentypen sind integer, boolean, string, range, dict, liste und  none.


####  E/A-Operationen und Dateiverarbeitung
Die Eingabe, Verarbeitung und Ausgabe von Daten mussten wir für folgende Punkte nutzen:
- Einlesen: Einlesen der XML-Datei, die zu einem Dictionary umgewandelt wurde.
- Verarbeitung: 
	- Die Antworten und Fragen wurden über die random Funktion ausgewählt und übergeben
	- Für die Übergabe der Daten brauchten wir eine Flask Schnittstelle:
	- Die Antwortüberprüfung mit Übergabe der Daten von Python zu Typescript und zurück
- Ausgabe: Die übertragenen Daten wurden mittels eines Buttons mit Click Event ausgegeben


#### Operatoren
Die von uns verwendeten Operatoren waren:
- Zuweisungsoperator: = ; +=
- Vergleichsoperatoren: ==


#### Kontrollstrukturen
Wir haben zwei verschiedene Kontrollstrukturen verwendet. Diese sind eine IF-Else Anweisung und eine For-Schleife. Jede dieser Strukturen wurde von uns in unserem Code mehrmals verwendet.


#### Funktionen
Wir haben in unserem Projekt 2 Funktionen genutzt. Die eine Funktion heißt  questionOutput()  und hat eine globalen Variable. Sie wird zur Generierung der Fragen- und der Antwortreihenfolge genutzt.  Die zweite Funktion heißt responseCheck() und ist für die Überprüfung der Antworten verantwortlich.  Die Daten werden über return übertragen.

Return von Werten
Globale Variable gesetzt

#### Stringverarbeitung
Wir haben die Antwortüberprüfung mit einem Stringvergleich gelöst. Dieser erfolgt in den nachfolgenden Schritte:
1. Die XML-Datei wird von Python eingelesen und greift auf den gewünschten Stringwert zu
2. Die Reihenfolge der Fragen und Antworten werden ausgewählt und über Flask an TypeScript weitergegeben und ausgegeben. (Strings)
3. Der ausgewählt Anwortstring wird über Fetch an Python zurück gegeben und mit der Antwortüberprüfung mit dem Lösungsstring verglichen.
4. Die Korrektheit der Antwort wird mittels einem String und Flask an Typscript übergeben und ausgegeben.

#### Strukturierte Datentypen

Die verwendeten Strukturierte Datentypen sind eine List und ein Dictionary.
Die Liste wurde von uns benötigt um keine Wiederholungen in den Fragen zu haben.
![[Pasted image 20240225144342.png]]
![Pasted image 20240225144342](https://github.com/haaf-emily/Quizgame/assets/152873694/196b8011-2080-436d-a110-0c4263ef1212)

Das Dictionary wurde bei uns verwendet um die ganzen Fragen und Antworten zu speichern und mit ihnen zu arbeiten. 

### Sie können die Syntax und Semantik von Python (10)

![[Pasted image 20240222101657.png]]
![Pasted image 20240222101657](https://github.com/haaf-emily/Quizgame/assets/152873694/4ca8f1ed-5310-4d0c-b4f8-3d6ff4673848)


Wir sind auf diese Stelle im Code besonders stolz, da sie alles abbildet was wir in den drei Wochen im Backend gemacht haben. 
1. Zeile 75: Wir haben eine Schnittstelle mit Flask erstellt, die unsere Backend Programmierung in Python mit unsere Frontend Programmierung in TypeScript verbindet. Sie stellt die Daten für die Funktion responseCheck() bereit, sobald sie  Anfragen vom Type  POST oder OPTIONS bekommt.
2. Zeile 76 bis 99: Die Funktion responseCheck() ist für die Antwortüberprüfung zuständig und verarbeitet die bereit gestellten Daten von Fetch. Die Antwortüberprüfung wird über eine String abfrage erledigt. Dies hat den Vorteil, damit die Random- Faktoren  vernachlässigt werden können. Da bei Beginn die Antworten in einer zufälligen Reihenfolgen ausgegeben werden und man so nicht mehr die statische Reihenfolge der XML-Datei existiert. Der übermittelte Stringwert wird mit dem String der answer4 überprüft. Die Frage erhält man über die globale Variable questions_key, die gespeichert hat welche Frage gerade an der Reihe ist,  und mit answer4, die den Lösungsstring enthält.  Anschließend wird über die Variable correct, die die Werte Richtig oder Falsch annehmen kann, mit return Zeile 99 über Flask  an Typescript übergeben.
3. Zeile 87: Wir haben die Möglichkeit gefunden dynamische Variablen zu nutzen statt statische. Dies hatte den Vorteil das wir uns eine Menge Code einsparen konnten und die Schnittstelle effizient zu gestalten.Diese Dynamische Variable ist dazu da,  dass wir die Abfrage der 4 Möglichen Antworten über eine Variable umsetzen. Wir haben in unsere XML-Datei die Antworten wie auch die Fragen über festgelegte ID´s unterschieden. Die Antworten gehen von Antwort1 bis Antwort4, wobei Antwort4 richtig ist. Über die unterschiedlichen Fragen, Frage1 bis Frage10, werden die Antwortmöglichkeiten unterschieden.


### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
![[Pasted image 20240225150806.png]]
![Pasted image 20240225150806](https://github.com/haaf-emily/Quizgame/assets/152873694/7f540f73-8bf5-4942-a9bc-aedcfd39a783)

Das Projekt wurde von der gesamten Gruppe zu gleichen Teilen bearbeitet. Dabei haben wir die ersten Überlegungen aufgeteilt in die drei Teile: Python Konzept, Schnittstellenfindung und Oberflächen Design.

Durch unsere unsere unterschiedlichen Kenntnisstände und größten Lernerfolg zu erzielen. Haben wir als Gruppe entschlossen jede Programmierung zu dritt durchzuführen. Die Programmierung erfolgte immer auf einem Laptop, sodass die Git Kommentare so zu werten sind, dass diese Personen den Code aufgeschrieben hat. So konnten wir Probleme umgehen, die in der Gruppe wegen den Installationen aufgetreten sind.
Die Programmierung erfolgte immer zu Dritt entweder in Präsens oder Online über Discord. 

Nach jedem zwischen Zwischenschritt wurde durch Debuggen der Code auf seine Funktionsfähigkeit überprüft. Erst wenn der Code fehlerfrei durch gelaufen ist sind wir zum nächsten Punkt gesprungen.

 Unser Vorgehen in der groben Übersicht:
 1. Ideenfindung der Bestandteile
 2. Festlegung vom Datentyp der Fragen- und Antwortspeicherung 
 3. XML-Datei erstellt und einlesen der Daten in Python
 4. Frage- und Antwortbereitstellung
 5. Oberflächenerstellung mit TypeScript und dem Framework React
 6. Schnittstellenprogrammierung mit Flask und Fetch
 7. Antwortüberprüfung 
 8. Testen des Programmes und letzte Anpassungen

Durch dieses Vorgehen konnten wir uns gegenseitig sehr gut helfen und so Frustration wegen nicht Finden von Fehlern umgehen können. 
Dieses Projekt werden wir auch zukünftig nutzen um uns ideal auf Klausuren, die auswendig lernen beinhalten vorzubereiten.

### Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

Dictionary:
Wir haben unsere Fragen und Antworten einer XML-Datei gespeichert, für die einfachere Erstellung. Um das ganze in Python verwenden zu können haben wir es in ein Dictionary umgewandelt und damit gearbeitet. 
![Pasted image 20240222112610](https://github.com/haaf-emily/Quizgame/assets/152873694/2907a1d8-3bad-4c0d-b96e-6b480b45e21b)

![[Pasted image 20240222112610.png]]
Liste:
Diese Liste benötigen wir  um  das erste Element aus der erstellten Liste zunehmen, damit das Programm funktioniert. Ohne kann das Programm nicht auf die Fragen zu greifen, da sie eine ganz andere Bezeichnung haben.
![[Pasted image 20240222112628.png]]
![Pasted image 20240222112628](https://github.com/haaf-emily/Quizgame/assets/152873694/a0740ef0-bfbf-47e0-b91a-e7c907f714b7)



## METHODENKOMPETENZ (10 Punkte)

### Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
Wir haben in unserem Projekt folgende Umgebungen verwendet:
- Git![[Pasted image 20240222114152.png]]
  ![Pasted image 20240222114152](https://github.com/haaf-emily/Quizgame/assets/152873694/97bc6272-f023-4f2c-b143-004618720b1d)

- Visual Studio Code![[Pasted image 20240222114210.png]]
![Pasted image 20240222114210](https://github.com/haaf-emily/Quizgame/assets/152873694/93806d99-49fb-45ee-a5cc-1c45de3236c0)

- Anaconda![[Pasted image 20240222114332.png]]
  ![Pasted image 20240222114332](https://github.com/haaf-emily/Quizgame/assets/152873694/aa8295e1-a181-4612-9aff-4e994dba435b)

- SourceTree![[Pasted image 20240222114449.png]]
  ![Pasted image 20240222114449](https://github.com/haaf-emily/Quizgame/assets/152873694/49efb942-7e5d-4a6c-aa57-1278ae5aca69)


Die Verwendung der verschiedenen Entwicklungsumgebungen können wir nicht objektiv darstellen bzw. begründen.

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

### Die Studierenden können ihre Software erläutern und begründen. (5)

Ja wir können als unseren Code erklären und begründen. Siehe Oben bei den einzelnen Punkten bei den wir auf die Funktionsweises unseres Codes hingewiesen haben.
Da der Code von uns gemeinsam erstellt wurde hat jeder den Code verstanden und kennt seine funktionsweise. Durch das Gegenseite Helfen und diskutieren welcher Code jetzt richtig ist haben wir diese Fähigkeit erlernt.

### Sie können existierenden Code analysieren und beurteilen. **(5)**
Wir haben die Gruppe Wissen ist Macht bewertet und diese Bewertung finden Sie in dem Ordner Grading Wissen ist Macht

### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

Ja, wir als Gruppe haben folgende neu Tools und Bibliotheken genutzt um unser Projekt zu erstellen:
Die Tools die wir verwendet haben waren Anaconda und Sourcetree

Wir haben unsere Wissen mit folgenden Bibliotheken und Frameworks erweiter:
- Oberfläche:
	- Node.js
	- TypeScript
	- CSS
	- Framework React
- Schnittstellenprogrammierung:
	- Fetch
	- Flask
	- Einlesen von der XML Datei
- XML-Datei

  

<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->


## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
- Dynamische Variablen. Begründung siehe Oben
- Schnittstellenprogrammierung: 
	 Wir sind stolz das unsere Schnittstelle funktioniert, da uns React Schwierigkeiten  bereitet hat. Unsere Lösung war von Python auf TypeScript -->Flask und von TypeScript auf Python --> Felch. Wir haben sehr lange versucht diese Schnittstelle hauptsächlich in Python zu programmieren, dies hat jedoch nicht funktioniert so das wir auf unsere jetzige Lösung zurück greifen mussten. 
	 
	Einbindung in Python: 
	 ![[Pasted image 20240222120453.png]]
  	![Pasted image 20240222120453](https://github.com/haaf-emily/Quizgame/assets/152873694/a082296d-45c3-45c4-bf0f-d45f403ca5a6)

	 
	 Schnittstelle in TypeScript:![[Pasted image 20240222120532.png]]
  					![Pasted image 20240222120532](https://github.com/haaf-emily/Quizgame/assets/152873694/e777dba6-0a2e-402a-be8d-059a161ed4e5)

- Benutzung Framework React: Wir haben uns als Gruppe bewusst dazu entschieden ein Framework zu verwenden und den Umgang mit einem Webframework zu lernen. Diese ersten Kenntnisse werden uns im späteren Verlauf des Studiums nützlich sein. Da wir vorher keine Berührungspunkte damit hatten sieht unser Endergebnis gut aus. In unserem Projekt haben wir den Fokus auf das Backend gelegt und hatten wir Schwierigkeiten bei der Installation des Frameworks.
	 ![[Pasted image 20240222121240.png]]
  	![Pasted image 20240222121240](https://github.com/haaf-emily/Quizgame/assets/152873694/27d8b74d-daa3-454d-af4c-f307b9e8fb03)

- Die weiteren Punkte auf die wir als Gruppe stolz sind werden oben beschrieben und erklärt 
	 --> z.B Stringverarbeitung und Dictionary
	 
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

##### Was lief gut?
Wir hatten einen sehr guten Überblick über unsere Aufgaben, durch die Ideenfindung am Anfang. Ebenfalls konnten wir  durch die Teamprogrammierung die Rechercheaufgaben gut einteilen und haben für Probleme in kürzere Zeit Lösungen gefunden. 

##### Wo hatten wir Schwierigkeiten?
- Bibliotheken finden und einarbeiten: Die nötigen Kenntnisse welche Bibliotheken es gibt und wir brauchten hatten wir am Anfang nicht. Deshalb mussten wir intensiv nach den passenden Lösungen suchen. 
- Fehlersuche: Die Fehlersuche bei den neu erlernten Inhalte hat uns Zeit gekostet, da wir uns in die ganzen Themen und Fehlerquellen und -codes erst einarbeiten mussten.
- Schnittstellenprogrammierung: Das Wissen der passenden Implementierung hat uns gefehlt. Weiteres siehe Oben.
- Bei der Frage: Wie programmiert man richtig im Team?
	 Unsere Lösung auf die Frage war das wir als Team gemeinsam alles Programmieren.
- Zeitmanagement:  Aufgrund der vielen Schwierigkeiten wurde unser Aufgabeneinteilung nach hinten verschoben, sodass wir erst kurz vorher fertig wurden.
	 --> Zur Verbesserung unsere Zeitmanagements gibt es keine Punkte, da wir Probleme bei der Umsetzung des Codes hatten und nicht bei der Einteilung der Vorarbeit.

#### Learning Outcomes
Die Lernerfolge wurden gemeinsam als Gruppe erreicht:
- Grundkenntnisse in Python verfestigen und Erweitern
- Datenbankverwendung über die XML-Datei
- Datentypen: Die genaue Verwendung von ihnen und das man auch externe Dateiformate in Dictionary umwandeln kann.
- TypeScript: Erlernung der Grundlagen und handeling damit
- Framework React: Umgang mit vorgefertigten Designblöcken und personalisieren der Standartdesigns.
- Schnittstellenprogrammierung von Python und React: Flask und Fetch
- Teamprogrammierung
- Zeitmanagement von Programmierprojekten
