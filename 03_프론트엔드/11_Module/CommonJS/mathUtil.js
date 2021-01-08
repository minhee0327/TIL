const PI = 3.14;
const getCircleArea = r => r*r * PI;

/*
//1. 모듈 객체를 사용해서 내보내는 경우
module.exports = {
    PI,
    getCircleArea
}
*/

//2. exports 키워드를 사용해서 내보내는 경우
exports.PI = PI;
exports.getCircleArea = getCircleArea;

// 내보낼 때는 통일감 있게 내보낼것.