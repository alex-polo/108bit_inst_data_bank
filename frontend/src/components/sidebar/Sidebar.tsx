import { Button, Nav, Navbar, Offcanvas } from 'react-bootstrap';
import { ReactElement, useState } from 'react';

import styles from './Sidebar.module.css';

function Sidebar(): ReactElement {
  const navClassName: string = `${styles.sidebar}`;

  const [show, setShow] = useState(true);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  // handleClose()

  return (
    <>
      <Nav defaultActiveKey="/home" className={navClassName}>
        <div className="sidebar-content">
          <div className="scrollbar-container">
            <a className="navbar-brand" href="/">
              <span>Data Bank</span>
            </a>
            <div className="sidebar-nav">
              <Nav.Link href="/dashboard/statistics">Статистика</Nav.Link>
              <Nav.Link eventKey="link-1">Link</Nav.Link>
              <Nav.Link eventKey="link-2">Link</Nav.Link>
              <Nav.Link eventKey="disabled" disabled>
                Disabled
              </Nav.Link>
            </div>
          </div>
        </div>
      </Nav>

      {/* <Nav>
      <Nav.Item>
        <Nav.Link href="/home">Active</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-1">Link</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="link-2">Link</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link eventKey="disabled" disabled>
          Disabled
        </Nav.Link>
      </Nav.Item>
    </Nav> */}
    </>
  );
}

export default Sidebar;
