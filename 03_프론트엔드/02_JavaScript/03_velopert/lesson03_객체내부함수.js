const dog = {
    name: '멍멍이',
    sound: '멍멍!',
    say: function () {
        console.log(this.sound);
    }
}

// 객체 내부에 함수가 들어가면, this는 자신이 속한 객체를 가리킴
// function으로 선언한 경우는 가능하지만, 화살표함수는 안됨
dog.say();
