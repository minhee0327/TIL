import React from "react";

const profileData = {
  minhee0327: {
    name: "강민희",
    description: "Frontend Engineer 가 되고 싶다 >_<!힣",
  },
  ez0: {
    name: "jamie",
    description: "똑순이",
  },
};

const Profile = ({ match }) => {
  const { username } = match.params;
  const profile = profileData[username];
  console.log(username);
  if (!profile) {
    return <div>존재하지 않는 이름 입니다.</div>;
  }

  return (
    <div>
      <h3>
        {username}({profile.name})
      </h3>
      <p>{profile.description}</p>
    </div>
  );
};

export default Profile;
