import React, { Component } from 'react';
import { Row,Col } from 'react-flexbox-grid';

class Entrevista extends Component {

  render(){
    return (
      <Row className="Entrevista pt-card" center="xs">
        <Col xs={12} style={{padding: 0}}>
            <Row start="xs">
              <Col className="Entrevista-Title" xs={12}>
                <h5>Entrevista</h5>
              </Col>

            </Row>
        </Col>
      </Row>
    );
  }
}


export default Entrevista;
