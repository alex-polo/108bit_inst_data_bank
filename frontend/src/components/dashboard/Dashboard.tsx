import { ReactElement } from 'react';

import NaviBar from '../navibar/NaviBar';
import Sidebar from '../sidebar/Sidebar';
import DashboardWorkspace from '../dashboard_workspace/DashboardWorkspace';

import styles from './Dashboard.module.css';

function Dashboard(): ReactElement {
  return (
    <>
      <div className="wrapper">
        <Sidebar />
        <div className="main">
          <NaviBar />
          <DashboardWorkspace />
        </div>
      </div>
    </>
  );
}

export default Dashboard;
