import React, { Component } from 'react';
import { Row,Col } from 'react-flexbox-grid';
import TestForm from '../TestForm/TestForm'

class Roles extends Component {
  render(){
    return (
      <Col xs={12}>
        <h4 style={{marginBottom: 24, marginTop: 24}}>Selecciona un rol</h4>
        <div className="pt-select">
          <select onChange={(e) => console.log(e.target.value)}>
            <option selected>Selecciona un Rol</option>
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
    );
  }
}


export default Roles;
