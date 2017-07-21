import React, { Component } from 'react';
import { Row, Col } from 'react-flexbox-grid';
import isEmpty from 'lodash/isEmpty'

class Roles extends Component {

  constructor(props){
    super(props)
    this.state = {
      selected: 0
    }
  }

  getRequirement(value){
      this.setState({ selected: value }, () => {
        this.props.getRequirement(this.state.selected)
      })
  }

  renderRequirement(req){
    return req.keys.map( key => {
      if(key !== 'name'){
        return (
          <Col xs={12} style={{marginTop: 24}} >
            <p>El nivel de <strong>{key}</strong> debe ser: <strong>{req.data[key]}</strong> </p>
          </Col>
        )
      }
    })
  }

  render(){
    return (
      <Row>
        <Col xs={12}>
          <h4 style={{marginBottom: 24, marginTop: 24}}>Selecciona un rol</h4>
          <div className="pt-select">
            <select value={this.state.selected} onChange={(e) => { this.getRequirement(e.target.value) }}>
              <option value="0">Selecciona un Rol</option>
              <option value="1">Presidente</option>
              <option value="2">Vicepresidente</option>
              <option value="3">Asesor</option>
              <option value="4">Ingeniero de Proyectos</option>
              <option value="5">Jefe Departamento</option>
              <option value="6">Subjefe Departamento</option>
              <option value="7">Auditor</option>
              <option value="8">Contador</option>
              <option value="9">Enfermera</option>
              <option value="10">Medico General</option>
              <option value="11">Medico Especialista</option>
              <option value="12">Coordinador Planes Salud</option>
              <option value="13">Ayudante Mantenimiento</option>
              <option value="14">Auxiliar Aseo</option>
              <option value="14">Despachador Farmaceutica</option>
              <option value="15">Secretario</option>
              <option value="16">Guardia</option>
            </select>
          </div>
        </Col>
        { !isEmpty(this.props.requirements) ? <Col xs={12} style={{marginTop: 24}} >
              <h5>Un <strong>{ this.props.requirements.data['name'] }</strong> debe tener</h5>
              <p> 0: Nada &nbsp;&nbsp; 1: Bajo &nbsp;&nbsp; 2: Medio &nbsp;&nbsp; 3: Alto &nbsp;&nbsp; 4: Destacado  </p>
            </Col> : ''}
        { !isEmpty(this.props.requirements) ? this.renderRequirement(this.props.requirements) : ''}
      </Row>
    );
  }
}


export default Roles;
