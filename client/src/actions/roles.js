import axios from 'axios'
import { SubmissionError } from 'redux-form'
import { SET_REQUIREMENT } from './types'

export const setRequirement = (requirements) => {
  return {
    type: SET_REQUIREMENT,
    requirements,
  }
}

export const getRequirement = data => {
  return dispatch => {
    return axios.get('http://localhost:5000/api/role/'+data)
            .then((value) => {
              dispatch(setRequirement(value.data))
            })
            .catch((err) => {
              throw new SubmissionError({ _error: err.response.data.error })
            })
  }
}
