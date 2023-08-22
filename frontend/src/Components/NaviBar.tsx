import React from 'react';
import { Navbar, Nav, Button } from 'react-bootstrap';

function NaviBar() {
    return (
        <>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand>Data Bank</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"></Navbar.Toggle>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Navbar.Text>
                        Signed in as: <a href="#login">Mark Otto</a>
                    </Navbar.Text>
                    <Nav.Link>
                        
                    </Nav.Link>
                </Nav>
                <Nav>
                    <Button variant="primary">Log out</Button>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    </>
    )
}

export default NaviBar