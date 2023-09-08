import React, { ReactElement } from 'react';
import { Routes, Route } from 'react-router-dom';

import AuthForm from './components/auth/AuthForm';
import Dashboard from './components/dashboard/Dashboard';
import NotFoundPage from './components/not_found/not_found_page';

import './App.css';

function App(): ReactElement {
  return (
    <>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/auth" element={<AuthForm />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </>
  );
}

export default App;
