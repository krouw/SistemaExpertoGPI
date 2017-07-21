import React, { Component } from 'react';
import { Row,Col } from 'react-flexbox-grid';
import TestForm from '../TestForm/TestForm'
import Roles from '../Roles/Roles'
import classNames from 'classnames'

class Entrevista extends Component {

  constructor(){
    super()
    this.state = {
      tab: true
    }
  }

  changeTab(e){
    this.setState({ tab: !this.state.tab })
  }

  render(){

    const btnClass1 = classNames({
      'pt-button pt-icon-clipboard': true,
      'pt-active': this.state.tab,
    });

    const btnClass2 = classNames({
      'pt-button pt-icon-people': true,
      'pt-active': !this.state.tab,
    });

    return (
      <Row className="Entrevista pt-card" center="xs" style={{marginBottom:32}}>
        <Col xs={12} style={{padding: 0}}>
            <Row center="xs">
              <Col className="Entrevista-Title" xs={12}>
                <div className="pt-button-group pt-large">
                  <a
                    className={btnClass1}
                    tabindex="0"
                    onClick={ (e) => this.changeTab(e)}
                    role="button">
                      Entrevista
                  </a>
                  <a
                    className={btnClass2}
                    tabindex="0"
                    onClick={ (e) => this.changeTab(e)}
                    role="button">
                    Roles
                  </a>
                </div>
              </Col>
            </Row>
            <Row start="xs">
              <Col xs={12}>
                { this.state.tab ? <TestForm /> : <Roles />}
              </Col>
            </Row>
        </Col>
      </Row>
    );
  }
}


export default Entrevista;
