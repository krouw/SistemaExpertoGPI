import React from 'react'
import { Row, Col } from 'react-flexbox-grid';
import InputTest from '../InputTest/InputTest'

const Topic = ({ data }) => {
    const questions = data.questions.map((question) =>{
        return (
          <Row>
            <Col xs={12}>
              <p style={{marginBottom: 16, marginTop: 16}}>{question.id_question}. {question.text}</p>
              <Row>
                <InputTest name={question.id_question} value="0" title="Nunca" />
                <InputTest name={question.id_question} value="0.25" title="Poco" />
                <InputTest name={question.id_question} value="0.50" title="Bastante" />
                <InputTest name={question.id_question} value="1" title="Siempre" />
              </Row>
            </Col>
          </Row>
        )
      });
    return (
      <Col xs={12}>
        <h4 style={{marginBottom: 24, marginTop: 24}}>{data.name}</h4>
        { questions }
      </Col>
    )
}

export default Topic
