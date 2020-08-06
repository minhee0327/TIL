import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import Post from "../components/Post";
import { getPost } from "../modules/posts";

function PostContainer({ postId }) {
  const { data, loading, error } = useSelector(
    (state) => state.posts.post[postId]
  ) || {
    loading: false,
    data: null,
    error: null,
  };
  const dispatch = useDispatch();

  useEffect(() => {
    if (data) return;
    dispatch(getPost(postId));
  }, [data, postId, dispatch]);

  if (loading) return <div>로딩중....</div>;
  if (!data) return null;
  if (error) return <div>에러발생!!</div>;

  return <Post post={data} />;
}

export default PostContainer;
