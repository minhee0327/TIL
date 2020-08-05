import * as postsAPI from "../api/posts";
import {createPromiseThunk, reducerUtils, handleAsyncActions} from '../lib/asyncUtils';

/* 액션타입 */
const GET_POSTS = 'GET_POSTS';
const GET_POSTS_SUCCESS = 'GET_POSTS_SUCCESS';
const GET_POSTS_ERROR = 'GET_POSTS_ERROR'

const GET_POST = 'GET_POST';
const GET_POST_SUCCESS = 'GET_POST_SUCCESS';
const GET_POST_ERROR = 'GET_POST_ERROR'


export const getPosts = createPromiseThunk('GET_POSTS', postsAPI.getPosts);
export const getPost = createPromiseThunk('GET_POST', postsAPI.getPostById)
// export const getPost = createPromiseThunk('GET_POST', postAPI.getPostsById(id))

const initialState = {
    posts:reducerUtils.initial(),
    post:reducerUtils.initial()
}

export default function posts(state = initialState, action){
    switch (action.type) {
        case GET_POSTS:
        case GET_POSTS_SUCCESS:
        case GET_POSTS_ERROR:
            return handleAsyncActions(GET_POSTS,'posts')(state,action)
        case GET_POST:
        case GET_POST_SUCCESS:
        case GET_POST_ERROR:
            return handleAsyncActions(GET_POST,'post')(state, action)
    
        default:
            return state;
    }
}