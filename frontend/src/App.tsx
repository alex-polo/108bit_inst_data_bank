import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import NaviBar from './components/NaviBar';
import { Routes, Route } from 'react-router-dom';
import AuthForm from './components/auth/AuthForm';
import NotFoundPage from './components/not_found/not_found_page';

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
      <Routes>
        <Route path="/auth" element={<AuthForm />} />
        <Route path="*" element={<AuthForm />} />
        {/* <Route path="*" element={<NotFoundPage />} /> */}
      </Routes>
    </div>
  );
}

export default App;
