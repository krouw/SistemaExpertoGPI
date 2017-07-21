import React, { Component } from 'react';
import { Row,Col } from 'react-flexbox-grid';
import TestForm from '../TestForm/TestForm'
import Roles from '../Roles/Roles'
import Result from '../../components/Result/Result'
import classNames from 'classnames'
import { connect } from 'react-redux'
import { getRoles } from '../../actions/test'
import { getRequirement } from '../../actions/roles'
import isEmpty from 'lodash/isEmpty'

class Entrevista extends Component {

  constructor(props){
    super(props)
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
                { this.state.tab ? <TestForm getRoles={ this.props.getRoles } /> : <Roles requirements={ this.props.requirements } getRequirement={ this.props.getRequirement } />}
              </Col>
            </Row>
        </Col>
        { !isEmpty(this.props.test.roles) ? <Result roles={this.props.test.roles} /> : '' }
      </Row>
    );
  }
}


function mapStateToProps(state){
  return {
    test: state.test,
    requirements: state.roles.requirements
  }
}

function mapDispatchToProps(dispatch){
  return {
    getRoles: (data) => dispatch(getRoles(data)),
    getRequirement: (data) => dispatch(getRequirement(data))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Entrevista)
