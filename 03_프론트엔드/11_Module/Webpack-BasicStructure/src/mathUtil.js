const PI = 3.14;
const getCircleArea = r => r*r * PI;
const getSquareArea = d => d* d;


//1. 모듈 객체를 사용해서 내보내는 경우
module.exports = {
    PI,
    getCircleArea,
    getSquareArea
}


//2. exports 키워드를 사용해서 내보내는 경우
// exports.PI = PI;
// exports.getCircleArea = getCircleArea;

