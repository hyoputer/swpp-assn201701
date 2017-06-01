import React from 'react';
import { connect } from 'react-redux';
import { toggle } from '../actions';

class Board extends React.Component {
    render() {
        return (
            <div>
                <table>
                    <tbody>
                        { this.props.board.map(row =>
                            <tr>
                                {row.map(block =>
                                    <th id={block.id} onClick={this.props.Toggle.bind(this, block.id)}>
                                    {block.value}
                                    </th>
                                )}
                            </tr>
                        )}
                    </tbody>
                </table>
                <label id='status_label'> { this.props.stat }</label>
            </div>
        )
    }
}

let mapStateToProps = (state) => {
    return {
        board: state.game.board,
        stat: state.game.stat,
    };
}

let mapDispatchToProps = (dispatch) => {
    return {
        Toggle: (id) => dispatch(toggle(id)),
    };
}

Board = connect(mapStateToProps, mapDispatchToProps)(Board);

export default Board;
