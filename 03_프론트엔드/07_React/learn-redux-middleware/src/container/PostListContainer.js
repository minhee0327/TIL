import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import Postist from "../components/PostList";
import { getPosts } from "../modules/posts";

function PostListContainer() {
  const { data, loading, error } = useSelector((state) => state.posts.posts);
  const dispatch = useDispatch();
  useEffect(() => {
    if (data) return;
    dispatch(getPosts());
  }, [data, dispatch]);
  // console.log(data, loading, error)

  if (loading) return <div>로딩중...</div>;
  if (!data) return null;
  if (error) return <div>error 발생 !!</div>;
  return <Postist posts={data} />;
}

export default PostListContainer;
