import { combineReducers } from 'redux';
import { TOGGLE, ENTER_ROOM_SUCCESS, START_GAME, RECIEVE_TOGGLE } from '../actions';

const x = new Array(19);
for (var i = 0; i < 19; i++) {
    x[i] = new Array(19);
    for(var j = 0; j < 19; j++)
        x[i][j] = {
            id: i.toString()+'_'+j.toString(),
            value: ' '
        };
};

const initialState = { 
    board: x,
    hash: "",
    roomid: "",
    username: "",
    stat: "",
    enemyname: "",
    f: null,
    turn: 1
};

const game = (state = initialState, action) => {
    switch (action.type) {
        case ENTER_ROOM_SUCCESS:
            return Object.assign({}, state,
            {
                board: state.board.map(row =>
                    row.map(block => {
                        return {
                            id: block.id,
                            value: '-'
                        };
                    })
                ),
                roomid: action.roomid,
                username: action.username,
                hash: action.hash,
                stat: "Waiting"
            });

        case START_GAME:
            return Object.assign({}, state,
            {
                enemyname: action.enemyname,
                stat: "Next O",
                f: action.f
            });

        case TOGGLE:
            return state

        case RECIEVE_TOGGLE:
            let slabel;

            if(action.win === 0) {
                if(state.turn % 2 === 0)
                    slabel = "Next O";
                else
                    slabel = "Next X";
            } else {
                if(action.win === 1)
                    slabel = "Win O";
                else
                    slabel = "Win X";
            }

            return Object.assign({}, state,
            {
                board: state.board.map(row =>
                    row.map(block => {
                        if (block.id !== action.id)
                            return block;
                        
                        if(state.stat === "Next O") {
                            return {
                                id: block.id,
                                value: 'O'
                            };
                        }
                        else {
                            return {
                                id: block.id,
                                value: 'X'
                            };
                        }
                    })
                ),

                stat: slabel,
                turn: state.turn + 1
            });

        default:
            return state;
    }
};

const omakApp = combineReducers({
    game
});

export default omakApp;
