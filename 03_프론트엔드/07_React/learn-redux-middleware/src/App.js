import React from "react";
// import CounterContainer from "./container/CounterContainer";
// import PostListContainer from './container/PostListContainer'
import { Route } from "react-router-dom";
import PostListPage from "./pages/PostListPage";
import PostPage from "./pages/PostPage";

function App() {
  return (
    <>
      {/* <CounterContainer /> */}
      <Route path="/" component={PostListPage} exact={true} />
      <Route path="/:id" component={PostPage} />
    </>
  );
}

export default App;
