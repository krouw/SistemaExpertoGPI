import axios from 'axios'
import { SubmissionError } from 'redux-form'
import { SET_ROLES } from './types'

export const setRoles = (roles) => {
  return {
    type: SET_ROLES,
    roles,
  }
}

export const getRoles = data => {
  return dispatch => {
    return axios.post('http://localhost:5000/api/test', data)
            .then((value) => {
              dispatch(setRoles(value.data.resultado))
            })
            .catch((err) => {
              throw new SubmissionError({ _error: err.response.data.error })
            })
  }
}
