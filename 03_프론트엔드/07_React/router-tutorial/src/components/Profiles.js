import React from "react";
import { NavLink, Route } from "react-router-dom";
import Profile from "./Profile";
import WithtouterSample from "./WithRouterSample";
import RouterHookSample from "./RouterHookSample";

const Profiles = () => {
  return (
    <div>
      <h3>유저목록: </h3>
      <ul>
        <li>
          <NavLink
            to="/profiles/minhee0327"
            activeStyle={{ background: "black", color: "white" }}
          >
            mini
          </NavLink>
        </li>
        <li>
          <NavLink
            to="/profiles/ez0"
            activeStyle={{ background: "black", color: "white" }}
          >
            jamie
          </NavLink>
        </li>
      </ul>
      <Route
        path="/profiles"
        exact
        render={() => <div>유저를 선택해 주세요</div>}
      />
      <Route path="/profiles/:username" component={Profile} />
      <WithtouterSample />
      <RouterHookSample />
    </div>
  );
};

export default Profiles;
