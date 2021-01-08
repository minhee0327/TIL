import React from 'react';
import PostContainer from '../container/PostContainer';

function PostPage({match}){
    const {id} = match.params;
    return <PostContainer postId={parseInt(id,10)}/>
}

export default PostPage