import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../modules";
import { addTodo, toggleTodo, removeTodo } from "../modules/todos";
import TodoList from "../components/TodoList";
import TodoInsert from "../components/TodoInsert";

function TodoApp() {
  const todos = useSelector((state: RootState) => state.todos);
  const dispatch = useDispatch();

  const onInsert = (text: string) => {
    dispatch(addTodo(text));
  };
  const onToggle = (id: number) => {
    dispatch(toggleTodo(id));
  };
  const onRemove = (id: number) => {
    dispatch(removeTodo(id));
  };

  return (
    <>
      <TodoInsert onInsert={onInsert} />
      <TodoList onToggle={onToggle} onRemove={onRemove} todos={todos} />
    </>
  );
}

export default TodoApp;
