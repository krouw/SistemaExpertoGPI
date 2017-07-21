import { SET_ROLES } from '../actions/types'

const initialState = {
  roles: []
}

export default (state = initialState, action = {}) => {
  switch (action.type) {
    case SET_ROLES:
      return Object.assign({}, state, {
              roles: action.roles,
             })
    default:
        return state;
  }
}
