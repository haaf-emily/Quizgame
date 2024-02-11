import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react";




function App() {
    const [message, setMessage] = useState('');
    const [question, setQuestion] = useState('');
    const [ant1, setAnswer1] = useState('');
    const [ant2, setAnswer2] = useState('');
    const [ant3, setAnswer3] = useState('');
    const [ant4, setAnswer4] = useState('');
    
    const [correct1, setCorrect1] = useState('');
    const [correct2, setCorrect2] = useState('');
    const [correct3, setCorrect3] = useState('');
    const [correct4, setCorrect4] = useState('');

    
      
    useEffect(() => {
      fetch('http://localhost:5000/api/questionOutput')
        .then(response => response.json())
        .then(data => setMessage(data.message))
        .catch(error => console.error('Error:', error));
    }, []);
    
    // Anfrage um Texte für Frage und Antworten zu bekommen
    async function getText() {
      const response = await fetch("http://localhost:5000/api/questionOutput");  
      const text = await response.json();
      console.log(text);

      if ('question' in text) {
        const receivedResult = text.question;
        setQuestion(` ${receivedResult}`);
      } else {
        setQuestion('No question found in the received data');
      }

      if ('answer1' in text){
        const receivedResult = text.answer1;
        setAnswer1(` ${receivedResult}`);
      } else {
        setAnswer1('No answer found in the received data');
      }


      if ('answer2' in text){
        const receivedResult = text.answer2;
        setAnswer2(` ${receivedResult}`);
      } else {
        setAnswer2('No answer found in the received data');
      }

      if ('answer3' in text){
        const receivedResult = text.answer3;
        setAnswer3(` ${receivedResult}`);
      } else {
        setAnswer3('No answer found in the received data');
      }


      if ('answer4' in text){
        const receivedResult = text.answer4;
        setAnswer4(` ${receivedResult}`);
      } else {
        setAnswer4('No answer found in the received data');
      }
    }
    
    const startClick = async () => {
      
      getText();
      
      setCorrect1(' ')
      setCorrect2(' ')
      setCorrect3(' ')
      setCorrect4(' ')
    }



    const ant1Click = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/responseCheck', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ selectedAnswer: ant1}), 
        });

        const result = await response.json();
        console.log(result);

        

        if ('correct' in result) {
          const receivedResult = result.correct;
          setCorrect1(` ${receivedResult}`);
        } else {
          setCorrect1('No result found in the received data');
        }
        


      } catch (error) {
        console.error('Error:', error);
      }
    };

    const ant2Click = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/responseCheck', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ selectedAnswer: ant2}), 
        });

        const result = await response.json();
        console.log(result);

        if ('correct' in result) {
          const receivedResult = result.correct;
          setCorrect2(` ${receivedResult}`);
        } else {
          setCorrect2('No result found in the received data');
        }
        


      } catch (error) {
        console.error('Error:', error);
      }
    };

    const ant3Click = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/responseCheck', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ selectedAnswer: ant3 }), 
        });

        const result = await response.json();
        console.log(result);
        
        if ('correct' in result) {
          const receivedResult = result.correct;
          setCorrect3(` ${receivedResult}`);
        } else {
          setCorrect3('No result found in the received data');
        }


      } catch (error) {
        console.error('Error:', error);
      }
    };


    const ant4Click = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/responseCheck', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ selectedAnswer: ant4}), 
        });

        const result = await response.json();
        console.log(result);
        
        if ('correct' in result) {
          const receivedResult = result.correct;
          setCorrect4(` ${receivedResult}`);
        } else {
          setCorrect4('No result found in the received data');
        }


      } catch (error) {
        console.error('Error:', error);
      }
    };


  


    return (
      <div className="App">
        <header className="App-header">

          <p>
          {message}<br/>
          <button onClick={startClick} >Start</button>
          <button onClick={startClick} >Nächste Frage</button><br/>
          {question}
               

          </p>

          <button onClick={ant1Click} >1: {ant1}</button> {correct1} <br/>
          <button onClick={ant2Click} >2: {ant2}</button> {correct2}<br/>
          <button onClick={ant3Click} >3: {ant3}</button> {correct3} <br/>
          <button onClick={ant4Click} >4: {ant4}</button> {correct4} <br/>
          
        </header>

          
      </div>
    );
}

export default App;


