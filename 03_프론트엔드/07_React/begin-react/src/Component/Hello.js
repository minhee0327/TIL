import React from 'react';

function Hello({ name, color, isSpecial }) {
    // const { name, color } = props
    return <div style={{ color: color }}>{isSpecial && <b>*</b>}안녕하세요? {name}</div>
}

Hello.defaultProps = {
    name: '이름없음'
}

export default Hello;