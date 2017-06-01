import React from 'react';
import ReactDOM from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga'
import { rootSaga } from './sagas'
import { Provider  } from 'react-redux';
import App from './components/App';
import omakApp from './reducers';

const sagaMiddleware = createSagaMiddleware();
const store = createStore(omakApp, applyMiddleware(sagaMiddleware));
const appElement = document.getElementById('root');

sagaMiddleware.run(rootSaga);



ReactDOM.render(
	<Provider store={store}>
		<App />
	</Provider>,
	appElement
);
