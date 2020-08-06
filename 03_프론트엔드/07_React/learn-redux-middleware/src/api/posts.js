import axios from "axios";

export const getPosts = async () => {
  const response = await axios.get("/posts");
  // console.log(response);
  return response.data;
};

export const getPostById = async (id) => {
  const response = await axios.get(`/posts/${id}`);
  return response.data;
};
