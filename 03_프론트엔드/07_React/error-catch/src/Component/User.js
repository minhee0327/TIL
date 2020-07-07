import React from 'react';

function User({ user }) {
    // null checking
    // 리엑트 컴포넌트에서 null 렌더링. (결과: 아무것도 보이지 않음. error화면 안보임)
    // 보통 데이터를 network 요청 혹은 나중에 데이터를 받아오는 상황에서 
    // 데이터 없으면 null 보여줌 (혹은 <div>로딩중</div> 결과물 렌더링)
    // if (!user) {
    //     return null;
    // }
    return (
        <div>
            <div>
                <b>ID:</b> {user.id}
            </div>
            <div>
                <b>Username: </b>{user.username}
            </div>
        </div>
    )
}

export default User;