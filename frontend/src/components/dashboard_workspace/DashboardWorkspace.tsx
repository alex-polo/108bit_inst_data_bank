import { ReactElement, useState } from 'react';
import axios, { AxiosError, AxiosResponse } from 'axios';
import { Breadcrumb, Card, Container, Row } from 'react-bootstrap';

import styles from './DashboardWorkspace.module.css';

function countSites() {
  const apiURL = 'http://127.0.0.1:8000';

  axios
    .get(apiURL)
    .then((response: AxiosResponse) => {
      console.log(response.data);
    })
    .catch((error: AxiosError) => {
      console.log(error.message);
    });
}

function DashboardWorkspace(): ReactElement {
  const [countResources, setCountResources] = useState(0);

  countSites();
  return (
    <>
      <Container fluid className="mt-4">
        <div className=""></div>
        <div className={styles.workspace}>
          <Breadcrumb>
            <Breadcrumb.Item href="/">Dashboard</Breadcrumb.Item>
            <Breadcrumb.Item href="https://getbootstrap.com/docs/4.0/components/breadcrumb/">Info</Breadcrumb.Item>
            <Breadcrumb.Item active>Data</Breadcrumb.Item>
          </Breadcrumb>
        </div>
        <Row>
          <Card>
            <Card.Header>Общее количество сайтов</Card.Header>
            <Card.Body>
              <Card.Text>{countResources}</Card.Text>
            </Card.Body>
          </Card>
          <Card>
            <Card.Header>Количество сайтов с ошибками</Card.Header>
            <Card.Body>
              <Card.Text>{countResources}</Card.Text>
            </Card.Body>
          </Card>
        </Row>
      </Container>
    </>
  );
}

export default DashboardWorkspace;
