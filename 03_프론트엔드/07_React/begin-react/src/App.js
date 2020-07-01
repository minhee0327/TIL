import React, { useRef, useState } from 'react';
import UserList from './Component/UserList';
import CreateUser from './Component/CreateUser';

function App() {
  const [inputs, setInputs] = useState({
    username: '',
    email: ''
  })

  const { username, email } = inputs;

  const onChange = (e) => {
    const { name, value } = e.target;
    setInputs({
      ...inputs,
      [name]: value
    });
  }

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

  const onCreate = () => {
    const user = {
      id: nextId.current,
      username,
      email
    }
    setUsers(users.concat(user))
    setInputs({
      username: '',
      email: ''
    })
    nextId.current += 1;
  }

  const onRemove = id => {
    setUsers(users.filter(user => user.id !== id))
  }

  const onToggle = id => {
    setUsers(users.map(user => user.id === id ? { ...user, active: !user.active } : user))
  }


  return (
    <>
      <CreateUser onChange={onChange} onCreate={onCreate} username={username} email={email} />
      <UserList users={users} onRemove={onRemove} onToggle={onToggle} />
    </>
  );
}

export default App;
