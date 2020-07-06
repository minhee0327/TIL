import React, { useReducer, useMemo } from 'react';
import UserList from './Component/UserList';
import CreateUser from './Component/CreateUser';
import produce from 'immer';

function countAcitveUsers(users) {
  console.log('활성 사용자 수를 세는중...');
  return users.filter(user => user.active).length;
}

const initialState = {
  inputs: {
    username: '',
    email: ''
  },
  users: [
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
  ]
}

function reducer(state, action) {
  switch (action.type) {
    case 'CREATE_USER':
      return produce(state, draft => {
        draft.users.push(action.user);
      })
    case 'TOGGLE_USER':
      return produce(state, draft => {
        const user = draft.users.find(user => user.id === action.id);
        user.active = !user.active;
      })
    case 'REMOVE_USER':
      return produce(state, draft => {
        const index = draft.users.findIndex(user => user.id === action.id);
        draft.users.splice(index, 1);
      })
    default:
      return state;
  }
}

export const UserDispatch = React.createContext(null);


function App() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const { users } = state;
  const count = useMemo(() => countAcitveUsers(users), [users]);

  return (
    <UserDispatch.Provider value={dispatch}>
      <CreateUser />
      <UserList users={users} />
      <div>활성화된 user수 :{count}</div>
    </UserDispatch.Provider>
  );
}

export default App;
