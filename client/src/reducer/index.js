import { combineReducers } from 'redux'
import { reducer as formReducer } from 'redux-form'
import test from './test'

const rootReducer = combineReducers({
  form: formReducer,
  test
});

export default rootReducer;
