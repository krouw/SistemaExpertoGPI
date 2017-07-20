import React, { Component } from 'react';
import { Row,Col } from 'react-flexbox-grid';
import TestForm from '../TestForm/TestForm'

class Entrevista extends Component {

  render(){
    return (
      <Row className="Entrevista pt-card" center="xs" style={{marginBottom:32}}>
        <Col xs={12} style={{padding: 0}}>
            <Row center="xs">
              <Col className="Entrevista-Title" xs={12}>
                <h2 style={{marginBottom: 38}}>Entrevista</h2>
              </Col>
            </Row>
            <Row start="xs">
              <Col xs={12}>
                <TestForm />
              </Col>
            </Row>
        </Col>
      </Row>
    );
  }
}


export default Entrevista;
