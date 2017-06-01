import React from 'react';
import { connect } from 'react-redux';
import { login } from '../actions';

const Login = ({ TryConnect, enemyname}) => {
    let inputn, inputp, inputr;
    const onSubmit = () => {
            TryConnect(inputn.value, inputp.value, inputr.value);
            inputp.value = "";
    };

    return (
        <div>
            <input ref={node => {inputn = node;}}placeholder="id" id="username_field"/>
            <input ref={node => {inputp = node;}}  placeholder="psw" id="password_field"/>
            <input ref={node => {inputr = node;}}  placeholder="room" id="room_field"/>
            <label id="enemy_field">{enemyname}</label>
            <button id="connect" onClick={onSubmit}>connect</button>
        </div>
    );
}

let mapStateToProps = (state) => {
    return {
        enemyname: state.game.enemyname
    };
}


let mapDispatchToProps = (dispatch) => {
    return {
        TryConnect: (username, password, roomid) => dispatch(login(username, password, roomid))
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);
