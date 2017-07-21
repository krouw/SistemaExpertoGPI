import { combineReducers } from 'redux'
import { reducer as formReducer } from 'redux-form'
import test from './test'
import roles from './roles'

const rootReducer = combineReducers({
  form: formReducer,
  test,
  roles
});

export default rootReducer;
