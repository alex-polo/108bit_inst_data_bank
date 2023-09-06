import React, { ReactElement, useState } from 'react';
import { Navbar, Nav, Button, Container, NavDropdown, Form } from 'react-bootstrap';

import styles from './NaviBar.module.css';

function NaviBar(): ReactElement {
  const [user_name, setUsername] = useState('Vincent');

  return (
    <>
      <Navbar expand="lg" className={styles.navibar}>
        <Container fluid>
          <Navbar.Brand href="/home">Data Bank</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Button className="my-2 my-lg-0">
              <span className="navbar-toggler-icon"></span>
            </Button>
            <Nav className="me-auto my-2 my-lg-0" style={{ maxHeight: '100px' }} navbarScroll>
              <Nav.Link href="#action2">Link</Nav.Link>
              <Nav.Link href="#" disabled>
                Link
              </Nav.Link>
            </Nav>
            <NavDropdown title="Notification" id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action4">Another action</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action5">Sign out</NavDropdown.Item>
            </NavDropdown>
            {/* <span>Вход выполнен:&nbsp;</span> */}
            <NavDropdown title={user_name} id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action4">Another action</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action5">Sign out</NavDropdown.Item>
            </NavDropdown>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}

export default NaviBar;
