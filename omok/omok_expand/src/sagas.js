import { take, put, call, fork, spawn, select } from 'redux-saga/effects'
import { delay } from 'redux-saga'
import {LOGIN, enterRoomSuccess, ENTER_ROOM_SUCCESS, GET_ACCEPT_ENEMY_REQUEST, getAcceptEnemyRequest, startGame, TOGGLE, recieveToggle, START_GAME} from './actions'

function players_url(roomid) {
    return 'http://13.124.80.116:8000/rooms/'+roomid+'/players/';
}

function user_url(uid) {
    return 'http://13.124.80.116:8000/users/'+uid+'/';
}

function history_url(roomid) {
    return 'http://13.124.80.116:8000/rooms/'+roomid+'/history/';
}

function room_url(roomid) {
    return 'http://13.124.80.116:8000/rooms/'+roomid+'/';
}

function fetchfunction(url, init) {
    return fetch(url, init)
    .then((resp) => resp.json()) 
    .then(function(data) {
        return data;
    });
}


export function* postEnterRoom(data) {
    let uname = data.username;
    let upwd = data.password;
    let roomid = data.roomid;

    const hash = new Buffer(`${uname}:${upwd}`).toString('base64');
    const post = yield call(fetch, players_url(roomid), {
        method: 'POST',
        headers: {
            'Authorization': `Basic ${hash}`
        }
    });
    console.log(post);
    if(post.ok) {
        yield put (enterRoomSuccess(roomid, uname, hash));
    } 
}

export function* watchLogin() {
    while(true) {
        const data = yield take(LOGIN)
        yield call(postEnterRoom, data);
    }
}

export function* createEnemyWait() {
    const data = yield take(ENTER_ROOM_SUCCESS);
    console.log("enterroom");
    yield call(createNewAction, data);
}

export function* waitEnemy() {
    while(true) {
        console.log("waiting getacceptenemyrequest");
        const data = yield take(GET_ACCEPT_ENEMY_REQUEST);
        yield call(acceptEnemy, data)
    }
}

export function* acceptEnemy(data) {
    let roomid = data.roomid;
    let username = data.username;
    let hash = data.hash;

    console.log("get current player list");
    const res = yield call(fetchfunction, players_url(roomid), {
        method: 'GET',
        headers: {
            'Authorization': `Basic ${hash}`
        }
    });
    console.log(res);

    let usernames = []
    for (let i = 0; i < res.length; i++) {
        const ires = yield call(fetchfunction, user_url(res[i]), {
            method: 'GET',
            headers: {
                'Authorization': `Basic ${hash}`
            }
        });
        usernames.push(ires["username"]);
    }
    console.log(usernames);
    let f = 0;

    if(usernames.length === 2) {
        let enemyname = "";
        if (usernames[0] === username) {
            enemyname = usernames[1];
      }
        else {
            enemyname = usernames[0];
            f = 1;
        }

        yield put (startGame(enemyname, roomid, f));
    } else {
        yield spawn(createNewAction, {roomid, username, hash});
    }
}

export function* createNewAction(data) {
    const roomid = data.roomid;
    const username = data.username;
    const hash = data.hash;
    console.log("wait enemy");
    yield delay(1000);
    console.log("1sec passed");
    yield put(getAcceptEnemyRequest(roomid, username, hash));
}

export function* waitToggle() {

    while(true) {
        const state = yield select();
        console.log("state"+state.game.turn);
        const {id} = yield take (TOGGLE);
        const place = id.split("_");
        const payload = {
            "place_i": place[0],
            "place_j": place[1]
        };

        const datajs = JSON.stringify(payload);
        const response = yield call(fetch, history_url(state.game.roomid), {
            method: 'POST',
            headers: {
                'Authorization': `Basic ${state.game.hash}`,
                "Content-type": "application/json; charset=utf-8"
            },
            body: datajs
        });

        if(response.ok) {

            const query = yield call(fetchfunction, room_url(state.game.roomid), {
                method: 'GET',
                headers: {
                    'Authorization': `Basic ${state.game.hash}`
                }
            });

            yield put (recieveToggle(id, query["win"]));
            if(query["win"] !== 0)
                break;
            yield spawn(createNewReciever);
            break;
        }
    }
}

export function* createNewReciever() {
    while(true) {
        const state = yield select();
        yield delay(1000);
        console.log("togglewaitend");

        const query = yield call(fetchfunction, room_url(state.game.roomid), {
            method: 'GET',
            headers: {
                'Authorization': `Basic ${state.game.hash}`
            }
        });

        if(state.game.turn < query["turn"]) {
            const history = yield call(fetchfunction, history_url(state.game.roomid), {
                method: 'GET',
                headers: {
                    'Authorization': `Basic ${state.game.hash}`
                }
            });
            const rechis = history[history.length - 1];
            console.log(rechis);
            yield put(recieveToggle(rechis["place_i"] +"_"+ rechis["place_j"], query["win"]));
            if(query["win"] !== 0)
                break;
            yield spawn(waitToggle);
            break;
        }
    }
}

export function* checkTurn() {
    yield take(START_GAME);
    const state = yield select();
    if(state.game.f === 0) 
        yield spawn(waitToggle);
    else
        yield spawn(createNewReciever);
}

export function* rootSaga() {
    yield fork(watchLogin);
    yield fork(createEnemyWait);
    yield fork(waitEnemy);
    yield fork(checkTurn);
}
