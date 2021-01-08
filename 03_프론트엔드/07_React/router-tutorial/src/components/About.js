import React from "react";
import qs from "qs";

const About = ({ location }) => {
  const query = qs.parse(location.search, {
    ignoreQueryPrefix: true,
  });
  //   console.log(query);
  const detail = query.detail === "true";

  return (
    <div>
      <h1>소개</h1>
      <p>이 플젝은 리엑트 라우트 실습 예정입니다.</p>
      {detail && <p>추가적인 정보는 어쩌구 저쩌구~~~</p>}
    </div>
  );
};

export default About;
