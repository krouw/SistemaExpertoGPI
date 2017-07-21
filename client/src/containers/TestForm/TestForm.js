import React from 'react'
import { reduxForm } from 'redux-form'
import Topic from '../../components/Topic/Topic'
import { Row, Col } from 'react-flexbox-grid';
import data from '../../config/data'
import { Button, Intent } from '@blueprintjs/core'
import isEmpty from 'lodash/isEmpty'

const validate = values => {
  let errors = {}

  let aux = data.data.map((topic) => {

    const check = topic.questions.map((question) => {
      if(isEmpty(values[parseInt(question.id_question)])){
        errors[question.id_question] = 'Error'
        return ''
      }
    })
    return ''
  })
  return errors
}

let TestForm = props => {
  const { handleSubmit, reset, pristine, submitting, valid, error, getRoles } = props
  const renderTopics = data.data.map((topic) =>{
      return (
        <Topic key={topic.id_topic} data={topic} />
      )
    });
  return (
    <form onSubmit={ handleSubmit(getRoles) }>
      <Col xs={12}>
        <Row>
          { renderTopics }
        </Row>
        <Row start={'xs'} middle={'xs'}>
          <Col xs={6}>
            { !valid && !error ? <p style={{marginTop:24}}>* Debes completar la cuesta para enviar</p> : '' }
            { error && <strong style={{color:'red', marginTop:24}}>{error}</strong>}
          </Col>
          <Col xs={6}>
            <Button
              className="pt-large"
              type="button"
              style={{margin: 16,marginTop:24,marginBottom:0}}
              intent={Intent.DEFAULT}
              disabled={pristine || submitting}
              onClick={reset}
              text={'Limpiar'} />
            <Button
              className="pt-icon-tick pt-large"
              style={{margin: 16,marginTop:24,marginBottom:0}}
              intent={Intent.SUCCESS}
              disabled={!valid}
              loading={submitting}
              type="submit"
              text={'Enviar'} />
          </Col>
        </Row>
      </Col>
    </form>
  )
}

TestForm = reduxForm({
  // a unique name for the form
  form: 'test',
  validate
})(TestForm)

export default TestForm;
