import {Dispatch} from 'redux';
import {AsyncActionCreator} from 'typesafe-actions';

type AnyAsyncActionCreator = AsyncActionCreator<any, any, any>;

export default function createAsyncThunk <A extends AnyAsyncActionCreator, F extends (...params: any[]) =>Promise<any>>(
    AsyncActionCreator:A,
    promiseCreator: F
){
    type Params = Parameters<F>;
    return function thunk(...params: Params){
        return async(dispatch: Dispatch)=>{
            const {request, success, failure} = AsyncActionCreator;
            dispatch(request(undefined));
            try{
                const result = await promiseCreator(...params);
                dispatch(success(result))
            }catch(e){
                dispatch(failure(e));
            }
        }
    }
}