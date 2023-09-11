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
            <a className="" href="/">
              <span>Data Bank</span>
            </a>
            <div className="sidebar-nav">
              <Nav.Link href="/dashboard/info">Инфо</Nav.Link>
              <Nav.Link href="/dashboard/resources">Ресурсы</Nav.Link>
              <Nav.Link href="/dashboard/logging">Логгирование</Nav.Link>
              {/* <Nav.Link eventKey="link-1">Ресурсы</Nav.Link>
              <Nav.Link eventKey="link-2">Пользователи</Nav.Link>
              <Nav.Link eventKey="disabled" disabled>
                Disabled
              </Nav.Link> */}
            </div>
          </div>
        </div>
      </Nav>
    </>
  );
}

export default Sidebar;
