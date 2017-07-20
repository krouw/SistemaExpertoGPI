import React from 'react'
import { Col } from 'react-flexbox-grid'
import { Field } from 'redux-form'

const InputTest = (props) => {
    return (
      <Col xs={12} style={{marginLeft:16,marginRight:16,marginTop:8, marginBottom: 8}}>
        <label class="pt-control pt-radio pt-large">
          <Field component={(value) => {
              return (
                <input
                  type="radio"
                  value={value.input.value}
                  onChange={(e) => value.input.onChange(e)}
                  checked={ value.input.checked }
                  name={value.input.name} />
              )
            }}
            type="radio"
            name={props.name}
            value={props.value} />
          <span style={{marginLeft: 8}} class="pt-control-indicator"></span>
          { props.title }
        </label>
      </Col>
    )
}

export default InputTest
