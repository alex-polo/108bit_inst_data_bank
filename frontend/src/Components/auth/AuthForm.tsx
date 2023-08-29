import Container from 'react-bootstrap/Container';
import { ReactElement } from 'react';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Image from 'react-bootstrap/Image';
import Button from 'react-bootstrap/Button';
import logo from '../../logo.svg';
import './auth.css';

function AuthForm(): ReactElement {
    return (
        <>
        <div className='auth-form'>
        <Form>
                <h5>Вход</h5>
                <hr/>
                <Image className="auth-form__img" src={logo} />
                <Form.Group as={Row} controlId="formGridEmail">
                    <Form.Label>Логин</Form.Label>
                    <Form.Control type="text" placeholder="Логин" />
                </Form.Group>
                <Form.Group as={Row} controlId="formGridPassword">
                    <Form.Label>Пароль</Form.Label>
                    <Form.Control type="password" placeholder="Пароль" />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
        </>
    )
}

export default AuthForm;