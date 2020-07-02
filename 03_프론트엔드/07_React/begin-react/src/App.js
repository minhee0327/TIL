import React, { useRef, useState, useMemo, useCallback } from 'react';
import UserList from './Component/UserList';
import CreateUser from './Component/CreateUser';

function App() {
  const [inputs, setInputs] = useState({
    username: '',
    email: ''
  })

  const { username, email } = inputs;

  const onChange = useCallback((e) => {
    const { name, value } = e.target;
    setInputs(inputs => ({
      ...inputs,
      [name]: value
    }));
  }, [])

  const [users, setUsers] = useState([
    {
      id: 1,
      username: 'minhee0327',
      email: 'queen.minhee@gmail.com',
      active: true
    },
    {
      id: 2,
      username: 'itzjamie96',
      email: 'jamie96@gmail.com',
      active: false
    },
    {
      id: 3,
      username: 'morningmemo',
      email: 'morningmemo@gmail.com',
      active: false
    }
  ])

  const nextId = useRef(4)

  const onCreate = useCallback(() => {
    const user = {
      id: nextId.current,
      username,
      email
    }
    setUsers(users => users.concat(user))
    setInputs({
      username: '',
      email: ''
    })
    nextId.current += 1;
  }, [username, email])

  const onRemove = useCallback(id => {
    setUsers(users => users.filter(user => user.id !== id))
  }, [])

  const onToggle = useCallback(id => {
    setUsers(users => users.map(user => user.id === id ? { ...user, active: !user.active } : user))
  }, [])

  function countUsers(users) {
    console.log("활성화된 user수를 검색합니다.");
    return users.filter(user => user.active).length
  }

  const count = useMemo(() => countUsers(users), [users]);
  return (
    <>
      <CreateUser onChange={onChange} onCreate={onCreate} username={username} email={email} />
      <UserList users={users} onRemove={onRemove} onToggle={onToggle} />
      <div>활성화된 user수 : {count}</div>
    </>
  );
}

export default App;
