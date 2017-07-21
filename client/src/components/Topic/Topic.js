import React from 'react'
import { Row, Col } from 'react-flexbox-grid';
import InputTest from '../InputTest/InputTest'

const Topic = ({ data }) => {

    const renderInputs = (id, inputs) => {
      const mapInputs = inputs.map((input) => {
        return (
          <InputTest name={id} value={input.value} title={input.text} />
        )
      })
      return mapInputs
    }

    const renderQuestions = data.questions.map((question) => {
        return (
          <Row key={ question.id_question }>
            <Col xs={12}>
              <p style={{marginBottom: 16, marginTop: 16}}>{question.id_question}. {question.text}</p>
              <Row>
                { renderInputs(question.id_question, question.inputs) }
              </Row>
            </Col>
          </Row>
        )
      });
    return (
      <Col xs={12}>
        <h4 style={{marginBottom: 24, marginTop: 24}}>{data.name}</h4>
        { renderQuestions }
      </Col>
    )
}

export default Topic
