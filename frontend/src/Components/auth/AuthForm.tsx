import Container from 'react-bootstrap/Container';
import { ReactElement } from 'react';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Image from 'react-bootstrap/Image';
import Button from 'react-bootstrap/Button';
import logo from '../../logo.svg';
import auth_form__img from '../../assets/auth_form__img.jpg';
import './auth.css';
import { Card } from 'react-bootstrap';

function AuthForm(): ReactElement {
  return (
    <>
      <div className="account-pages pt-2 pt-sm-5 pb-4 pb-sm-5">
        <Container>
          <div className="justify-content-center row">
            <div className="col-xxl-4 col-xl-5 col-lg-6 col-md-8">
              <Card>
                {/* <Card.Img variant="top" src="holder.js/100px180" /> */}
                <Card.Img variant="top" src={auth_form__img} />
                <Card.Body>
                  {/* <Card.Title>Вход</Card.Title> */}
                  <div className="p-4 text-center w-75 m-auto">
                    <h4>Вход</h4>
                    <p className="text-muted mb-4">Введите логин и пароль для доступа к панели</p>
                  </div>

                  <Form className="p-4 mb-3">
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
                  {/* <Card.Text></Card.Text> */}
                  {/* <Button variant="primary">Go somewhere</Button> */}
                </Card.Body>
              </Card>
            </div>
          </div>
        </Container>
      </div>
    </>
  );
}

export default AuthForm;
