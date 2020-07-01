import React from 'react';

function CreateUser({ username, email, onChange, onCreate }) {
    return (
        <div>
            <input name="username" value={username} onChange={onChange} placeholder="계정명" />
            <input name="email" value={email} onChange={onChange} placeholder="이메일" />
            <button onClick={onCreate}>등록</button>
        </div>
    )
}

export default CreateUser;