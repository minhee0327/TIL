import React, { useContext } from 'react';
import { UserDispatch } from '../App';

const User = React.memo(function User({ user }) {
    const dispatch = useContext(UserDispatch);

    return (
        <div>
            <b onClick={() => dispatch({ type: 'TOGGLE_USER', id: user.id })} style={{ cursor: 'pointer', color: user.active ? 'green' : 'black' }} >
                {user.username}
            </b>
            <span>
                ({user.email})
            </span>
            <button onClick={() => dispatch({ type: 'REMOVE_USER', id: user.id })}>삭제</button>
        </div>
    )
});

function UserList({ users, onRemove, onToggle }) {
    return (
        <div>
            {users.map((user, idx) => (<User user={user} key={idx} onRemove={onRemove} onToggle={onToggle} />))}
        </div>
    )
}

export default React.memo(UserList);