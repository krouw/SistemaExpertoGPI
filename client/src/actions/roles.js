import axios from 'axios'
import { SubmissionError } from 'redux-form'
import { SET_REQUIREMENT, API } from './types'

export const setRequirement = (requirements) => {
  return {
    type: SET_REQUIREMENT,
    requirements,
  }
}

export const getRequirement = data => {
  return dispatch => {
    return axios.get(API+'/api/role/'+data)
            .then((value) => {
              dispatch(setRequirement(value.data))
            })
            .catch((err) => {
              throw new SubmissionError({ _error: err.response.data.error })
            })
  }
}
