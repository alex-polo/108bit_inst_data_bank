import Container from 'react-bootstrap/Container';
import { ReactElement } from 'react';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
// import Image from 'react-bootstrap/Image';
import Button from 'react-bootstrap/Button';
import auth_form__img from '../../assets/auth_form__img.jpg';
import styles from './AuthForm.module.css';
import { Card } from 'react-bootstrap';

function AuthForm(): ReactElement {
  const authFormClassName: string = `mb-3 ${styles.auth_form}`;

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
                  <div className="text-center w-75 m-auto">
                    <div className="p-2">
                      <h4>Вход</h4>
                      <p className="text-muted">Введите логин и пароль для доступа к панели</p>
                    </div>

                    <Form className={authFormClassName}>
                      <Form.Group as={Row} controlId="formGridEmail">
                        <Form.Label>Логин</Form.Label>
                        <Form.Control type="text" placeholder="Логин" />
                      </Form.Group>
                      <Form.Group className="mt-2" as={Row} controlId="formGridPassword">
                        <Form.Label>Пароль</Form.Label>
                        <Form.Control type="password" placeholder="Пароль" />
                      </Form.Group>
                      <Button className="mt-4" variant="primary" type="submit">
                        Войти
                      </Button>
                      {/* <Button size="sm" className="mt-4" variant="outline-success" type="submit">
                        Войти
                      </Button> */}
                    </Form>
                  </div>
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
