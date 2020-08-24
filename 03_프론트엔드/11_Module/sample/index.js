//node JS의 확장자가 기본으로 JS이기 때문에, .js를 삭제해도 작동가능
const {getCircleArea, getSquareArea} = require('./mathUtil')
const {logFigureError, logInput, logResult } = require('./log');

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output : process.stdout
})

rl.question(
    "넓이를 구하고자 하는 도형의 종류를 입력하세요. (정사각형, 원) : ",
    figure => {
        switch(figure){
            case '정사각형':
                rl.question('변의 길이를 입력하세요 : ', input =>{
                    console.log(logInput(input))
                    console.log(logResult(figure, getSquareArea(input)));
                    rl.close();
                })
                break;
            case '원':
                rl.question('반지름 길이를 입력하세요: ', input =>{
                    console.log(logInput(input));
                    console.log(logResult(figure, getCircleArea(input)));
                    rl.close();
                })
                break;
            default:
                console.log(logFigureError)
                rl.close();
        }
    }
)