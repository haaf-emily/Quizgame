import React from 'react';
import './App.css';import Radio from '@mui/material/Radio';

function MyButton({ title }: { title: string }) {
  
  return (
    <button>{title}</button> );

}
  function App() {
  return (
    <div className="App">
      <header className="App-header">
        
        
      

        <p>
          Frage 1:

        </p>

        <p>
        Antworten:
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
