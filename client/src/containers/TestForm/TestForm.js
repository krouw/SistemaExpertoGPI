import React from 'react'
import { reduxForm } from 'redux-form'
import Topic from '../../components/Topic/Topic'
import { Row, Col } from 'react-flexbox-grid';
import data from '../../config/data'
import { Button, Intent } from '@blueprintjs/core'

const submit = (value) => {
  console.log(value);
}

let TestForm = props => {
  const { handleSubmit, reset, pristine, submitting } = props
  const renderTopics = data.data.map((topic) =>{
      return (
        <Topic data={topic} />
      )
    });
  return (
    <form onSubmit={ handleSubmit(submit) }>
      <Col xs={12}>
        <Row>
          { renderTopics }
        </Row>
        <Row end={'xs'}>
          <Col xs={12}>
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
  form: 'test'
})(TestForm)

export default TestForm;
