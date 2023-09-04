import React from 'react';
import { Navbar, Nav, Button, Container } from 'react-bootstrap';

function NaviBar() {
    return <>
    <Navbar className="navbar-bg navbar navbar-expand navbar-light nvbar">
          <Container>
            <Navbar.Brand href="#home">Navbar with text</Navbar.Brand>
            <Navbar.Toggle />
            <Navbar.Collapse className="justify-content-end">
              <Navbar.Text>
                Signed in as: <a href="/login">Vincent</a>  
              </Navbar.Text>
            </Navbar.Collapse>
          </Container>
        </Navbar>
    </>
}

export default NaviBar