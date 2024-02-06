import React from 'react';
import logo from './logo.svg';
import './App.css';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import { useState, useEffect } from "react";

/*function MyButton({ title }: { title: string }) {
  return (
    <button onClick={handleClick} >{title}</button>
  );
}

*/
/*

function Myradio (){
    return (
    <RadioGroup
    aria-labelledby="demo-radio-buttons-group-label"
    
    name="radio-buttons-group"
    >
    <FormControlLabel value="answer1" control={<Radio />} label="Female" />
    <FormControlLabel value="answer2" control={<Radio />} label="Male" />
    <FormControlLabel value="answer3" control={<Radio />} label="Other" />
    <FormControlLabel value="answer4" control={<Radio />} label="x" />
    </RadioGroup>
    );
    <Myradio />
}
*/





function App() {
        const [message, setMessage] = useState('');

        useEffect(() => {
          fetch('http://localhost:5000/api/hello')
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error:', error));
        }, []);

      const handleClick = async () => {
        try {
          const response = await fetch('http://localhost:5000/api/process_data', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ key: 'Anwort 1' }), // Hier die Daten einfügen
          });

          const result = await response.json();
          console.log(result);
          setMessage(result.result);
        } catch (error) {
          console.error('Error:', error);
        }
      };


  


  return (
    <div className="App">
      <header className="App-header">


      <button onClick={handleClick} >Antwort 1</button>
        
        <h1>{message}</h1>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
          
        </a>

        <span
        style={{
          position: 'absolute',
          top: 0,
          right: 0,
          padding: '10px',
          background: 'rgba(0, 0, 0, 0.5)',
          color: 'white',
        }}
      >
        Oberer rechter Ecken-Text
      </span>
      </header>
    </div>
  );
}

export default App;


