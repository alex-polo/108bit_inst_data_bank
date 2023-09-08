import { ReactElement, useState } from 'react';
import { Breadcrumb, Card, Container, Row } from 'react-bootstrap';

import styles from './DashboardWorkspace.module.css';

function DashboardWorkspace(): ReactElement {
  const [countResources, setCountResources] = useState(0);
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
            <Card.Header>Количество ресурсов</Card.Header>
            <Card.Body>
              <Card.Text>{countResources}</Card.Text>
            </Card.Body>
          </Card>
          <Card>
            <Card.Body>
              <Card.Text>Количество сайтов: {countResources}</Card.Text>
            </Card.Body>
          </Card>
        </Row>
      </Container>
    </>
  );
}

export default DashboardWorkspace;
