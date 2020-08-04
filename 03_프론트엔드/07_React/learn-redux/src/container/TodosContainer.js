import React, { useCallback } from "react";
import { connect } from "react-redux";
import Todos from "../components/Todos";
import { toggleTodo, addTodo } from "../modules/todos";

function TodosContainer({ todos, addTodo, toggleTodo }) {
  const onCreate = (text) => addTodo(text);
  const onToggle = useCallback((id) => toggleTodo(id), [toggleTodo]);

  return <Todos todos={todos} onCreate={onCreate} onToggle={onToggle} />;
}

export default connect((state) => ({ todos: state.todos }), {
  addTodo,
  toggleTodo,
})(TodosContainer);
