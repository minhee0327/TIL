import { ActionType } from "typesafe-actions";
import * as actions from "./actions";

/* 액션객체에 대한 타입 */
export type TodosAction = ActionType<typeof actions>;
export type Todo = {
  id: number;
  text: string;
  done: boolean;
};
export type TodosState = Todo[];
