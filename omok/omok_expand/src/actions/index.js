export const TOGGLE = 'TOGGLE';
export const RESTART = 'RESTART';
export const LOGIN = 'LOGIN';
export const ENTER_ROOM_SUCCESS = 'ENTERROOMSUCCESS';
export const GET_ACCEPT_ENEMY_REQUEST = 'GETACCEPTENEMYREQUEST';
export const START_GAME = 'STARTGAME';
export const RECIEVE_TOGGLE = 'RECIEVETOGGLE';

export function toggle(id) {
    return {
        type: TOGGLE,
        id: id
    };
}

export function restart() {
    return {
        type: RESTART
    };
}

export function login(username, password, roomid) {
    return {
        type: LOGIN,
        username: username,
        password: password,
        roomid: roomid
    };
}

export function enterRoomSuccess(rid, uname, hash) {
    return {
        type: ENTER_ROOM_SUCCESS,
        username: uname,
        roomid: rid,
        hash: hash
    };
}

export function getAcceptEnemyRequest(rid, uname, hash) {
    return {
        type: GET_ACCEPT_ENEMY_REQUEST,
        roomid: rid,
        username: uname,
        hash: hash
    };
}

export function startGame(enemyname, roomid, f) {
    return {
        type: START_GAME,
        enemyname: enemyname,
        roomid: roomid,
        f: f
    };
}

export function recieveToggle(id, win) {
    return {
        type: RECIEVE_TOGGLE,
        id: id,
        win: win
    };
}
