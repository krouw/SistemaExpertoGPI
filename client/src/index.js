import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './containers/App';
import registerServiceWorker from './registerServiceWorker';
import Layout from './containers/Layout'
import { Provider } from 'react-redux'
import store from './config/store'

ReactDOM.render(<Provider store={store}>
                      <App>
                        <Layout /> </App>
                      </Provider>, document.getElementById('root'));
registerServiceWorker();
