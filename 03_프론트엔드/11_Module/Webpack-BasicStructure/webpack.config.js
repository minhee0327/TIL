//파일이 생성되는 경로이기 때문에, path정보의 경우 절대경로로 설정해야한다.
//노드에서 제공해주는 path 내장모듈 사용할 것

const path = require('path')

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js' 
    },
    //환경이 node라는 점을 설정
    target:'node'
}