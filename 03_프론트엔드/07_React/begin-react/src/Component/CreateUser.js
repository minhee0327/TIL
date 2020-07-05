import React, { useRef, useContext } from 'react';
import useInputs from '../hooks/useInputs';
import { UserDispatch } from '../App';

function CreateUser() {
    const [{ username, email }, onChange, reset] = useInputs({
        username: '',
        email: ''
    })

    const nextId = useRef(4);
    const dispatch = useContext(UserDispatch);

    const onCreate = () => {
        dispatch({ type: 'CREATE_USER', user: { id: nextId.current, username, email } })
        reset();
        nextId.current += 1;
    }

    return (
        <div>
            <input name="username" value={username} onChange={onChange} placeholder="계정명" />
            <input name="email" value={email} onChange={onChange} placeholder="이메일" />
            <button onClick={onCreate}>등록</button>
        </div>
    )
}

export default React.memo(CreateUser);