import React, { Fragment } from 'react';
import { Outlet } from 'react-router-dom';
import NavBar from '../../components/navbar/NavBar';
import './Base.css';

export default function Base() {
  return (
    <div className='root-container'>
      <NavBar />
      <main>
        <Outlet />
      </main>
    </div>
  );
}