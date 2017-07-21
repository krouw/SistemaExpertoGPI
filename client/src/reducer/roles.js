import { SET_REQUIREMENT } from '../actions/types'

const initialState = {
  requirements: {}
}

export default (state = initialState, action = {}) => {
  switch (action.type) {
    case SET_REQUIREMENT:
      return Object.assign({}, state, {
              requirements: action.requirements,
             })
    default:
        return state;
  }
}
