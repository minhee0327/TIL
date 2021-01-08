import {
  createStandardAction,
  createReducer,
  createAction,
  ActionType,
} from "typesafe-actions";

/* 액션타입 */
const ADD_TODO = "todos/ADD_TODO";
const TOGGLE_TODO = "todos/TOGGLE_TODO";
const REMOVE_TODO = "todos/REMOVE_TODO";

let nextId = 1;

/* 액션생성함수 */
export const addTodo = createAction(ADD_TODO, (action) => (text: string) =>
  action({
    id: nextId++,
    text,
  })
);
export const toggleTodo = createStandardAction(TOGGLE_TODO)<number>();
export const removeTodo = createStandardAction(REMOVE_TODO)<number>();

const actions = {
  addTodo,
  toggleTodo,
  removeTodo,
};

/* 액션객체에 대한 타입 */
type TodoAction = ActionType<typeof actions>;
export type Todo = {
  id: number;
  text: string;
  done: boolean;
};
export type TodosState = Todo[];
const initialState: TodosState = [];

const todos = createReducer<TodosState, TodoAction>(initialState, {
  [ADD_TODO]: (state, action) =>
    state.concat({ ...action.payload, done: false }),
  [TOGGLE_TODO]: (state, { payload: id }) =>
    state.map((todo) =>
      todo.id === id ? { ...todo, done: !todo.done } : todo
    ),
  [REMOVE_TODO]: (state, { payload: id }) =>
    state.filter((todo) => todo.id !== id),
});

export default todos;
