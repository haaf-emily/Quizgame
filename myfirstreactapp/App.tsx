import React from 'react';
import './App.css';import Radio from '@mui/material/Radio';
import TextField from '@mui/material/TextField';

function MyButton({ title }: { title: string }) {
  
  return (
    <button>{title}</button> );
  
}
  function App() {
  return (
    <div className="App">
      <header className="App-header">

        <p>
      
      
      <span
      style={{
        position: 'absolute',
        top: 0,
        right: 0,
        padding: '10px',
        background: 'rgba(0, 0, 0, 0,5)',
        color: 'black',
      }}
    >
      Score: <br/>    
      
      </span>
        </p>

        <span
      style={{
        position: 'absolute',
        top: 0,
        right: 120,
        padding: '10px',
        background: 'rgba(0, 0, 0, 0,5)',
        color: 'black',
      }}
    >
      Bisherige Fehler: <br/>    
      
      </span>
        <p>
          Frage 1:


        </p>
          <MyButton title=" Antwort 1" /> <br/>
          <MyButton title=" Antwort 2" /> <br/>
          <MyButton title=" Antwort 3" /> <br/>
          <MyButton title=" Antwort 4" /> <br/>
        
      </header>
      
    </div>
    
  
      );
    }

  


export default App;
