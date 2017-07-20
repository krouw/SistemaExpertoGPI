import React from 'react';
import { Row,Col } from 'react-flexbox-grid';
import Header from '../components/Header/Header';
import Entrevista from './Entrevista/Entrevista'

const Layout = () => {
  return (
    <section className="Layout">
      <Header />
      <Row className="Content" center="xs">
        <Col xs={11} sm={7} style={{padding:0}}>
          <Entrevista />
        </Col>
      </Row>
    </section>
  );
}


export default Layout;
