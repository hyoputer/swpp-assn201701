import React from 'react';
import Board from './Board';
import Login from './Login';

class App extends React.Component {
    render() {
        return (
            <div>
                <Login/>
                <Board/>
            </div>
        );
    }
}

export default App;
