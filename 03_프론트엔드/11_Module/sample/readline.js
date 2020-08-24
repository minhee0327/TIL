const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

// question method는 사용자에게 입력받기 전 메세지를 보여주고
// 입력한 데이터를 콜백함수로 다룰 수 있게 한다.
// 첫번째 param은 어떤 문자를 입력해야하는지 정보를 제공
// 두번째 param은 사용자 입력이 발생하면, 실행되는 call back 함수
// 입력받은 값을 전달받는다.
rl.question('원하는 도형을 작성해 주세요 : ', input => {
    console.log(input);
    rl.close();
})