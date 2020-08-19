import { AnyAction } from "redux";
import { getType, AsyncActionCreator } from "typesafe-actions";

export type AsyncState<T, E = any> = {
  data: T | null;
  loading: boolean;
  error: E | null;
};

export const asyncState = {
  initial: <T, E = any>(initialData?: T): AsyncState<T, E> => ({
    data: initialData || null,
    loading: false,
    error: null,
  }),
  load: <T, E = any>(data?: T): AsyncState<T, E> => ({
    data: data || null,
    loading: true,
    error: null,
  }),
  success: <T, E = any>(data: T): AsyncState<T, E> => ({
    data,
    loading: false,
    error: null,
  }),
  error: <T, E = any>(error: E): AsyncState<T, E> => ({
    data: null,
    loading: false,
    error: error,
  }),
};

type AnyAsyncActionCreator = AsyncActionCreator<any, any, any>;
export function createAsyncReducer<
  S,
  AC extends AnyAsyncActionCreator,
  K extends keyof S
>(AsyncActionCreator: AC, key: K) {
  return (state: S, action: AnyAction) => {
    const [request, success, failure] = [
      AsyncActionCreator.request,
      AsyncActionCreator.success,
      AsyncActionCreator.failure,
    ].map(getType);
    switch (action.type) {
      case request:
        return {
          ...state,
          [key]: asyncState.load(),
        };
      case success:
        return {
          ...state,
          [key]: asyncState.success(action.payload),
        };
      case failure:
        return {
          ...state,
          [key]: asyncState.error(action.payload),
        };
      default:
        return state;
    }
  };
}

export function transformToArray<AC extends AnyAsyncActionCreator>(
  AsyncActionCreator: AC
) {
  const { request, success, failure } = AsyncActionCreator;
  return [request, success, failure];
}
