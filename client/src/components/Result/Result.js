import React from 'react'
import { Row, Col } from 'react-flexbox-grid'

const Result = ({roles}) => {
  const renderResult = roles.map( role => {
      console.log(role);
      return (
        <Col key={role} xs={12} style={{marginBottom: 8}}>
          <strong style={{textTransform: 'capitalize'}}>* {role}</strong>
        </Col>
      )
  })
  return (
    <div>
      <Row center={'xs'} style={{marginTop: 32, marginBottom: 24}} >
        <Col xs={12}>
          <h2>Resultados</h2>
        </Col>
      </Row>
      <Row start={'xs'}>
        <Col xs={12} style={{marginBottom: 16}}>
          <h5>Los cargos a los que puedes optar son:</h5>
        </Col>
        { renderResult }
      </Row>
    </div>
  )
}

export default Result
