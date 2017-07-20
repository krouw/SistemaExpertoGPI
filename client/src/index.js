import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './containers/App';
import registerServiceWorker from './registerServiceWorker';
import Layout from './containers/Layout'

ReactDOM.render(<App> <Layout /> </App>, document.getElementById('root'));
registerServiceWorker();
