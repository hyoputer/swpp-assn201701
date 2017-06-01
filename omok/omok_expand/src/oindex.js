import React from 'react'
import ReactDOM from 'react-dom'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import App from './components/App'
import reducer from './reducers'
import { Component } from 'react'

var x = new Array(19);
for (var i = 0; i < 19; i++) {
    x[i] = new Array(19);
    for(var j = 0; j < 19; j++)
        x[i][j] = {
            id: i.toString()+j.toString(),
            value: '-'
        };
}

const initialState = x; 

const blocks = (state = initialState, action) => {
    switch (action.type) {
        case 'TOGGLE':
            return state.map(row => {
                return row.map(block => {
                    if(block.id !== action.id)
                        return block;

                    return {
                        ...block,
                        value: 'O'
                    };
                });
            });
            
        default:
            return state;
    }
};

const omakApp = (state = initialState, action) => {
    return {
        blocks: blocks(
            state.blocks,
            action
        )
    };
};

const store = createStore(omakApp);

class OmakApp extends Component {
    render() {
        return (
            <div>
                <table>
                    <tbody>
                        {this.props.blocks.map(row => 
                            <tr>
                                {row.map(block =>
                                    <th key={block.id}
                                        onClick={ () => {
                                            store.dispatch({
                                                type: 'TOGGLE',
                                                id: block.id
                                            });
                                        }}>
                                        {block.value}
                                    </th>
                                )}
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        );
    }
}

const render = () => {
    ReactDOM.render(
        <OmakApp blocks={store.getState().blocks} />,
        document.getElementById('root')
    );
};

store.subscribe(render);
render();
