import React from 'react';
import NaviBar from './components/navibar/NaviBar';
import { Routes, Route } from 'react-router-dom';
import AuthForm from './components/auth/AuthForm';
import Sidebar from './components/sidebar/Sidebar';
import NotFoundPage from './components/not_found/not_found_page';

import './App.css';

function App() {
  return (
    <div className="wrapper">
      <Sidebar />
      <div className="main">
        <NaviBar />
        <Routes>
          {/* <Route path="/auth" element={<AuthForm />} /> */}
          <Route path="*" element={<AuthForm />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </div>
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
    </div>
  );
}

export default App;
