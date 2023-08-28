import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import logo from './logo.svg';
import NaviBar from './Components/NaviBar';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AuthForm from './Components/auth/AuthForm';
import { QueryClient } from 'react-query';
import { useQuery } from 'react-query';
import axios from 'axios';


const queryClient = new QueryClient();


async function fetchData(){
  const response = await 
}

function App() {
  return (
    <div className="App">
      


      {/* <header className="App-header">
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
      </header> */}

      <NaviBar />
      <BrowserRouter>
        <Routes>
          <Route path="/auth" element={ <AuthForm /> } />
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App;
