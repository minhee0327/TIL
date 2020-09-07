var score1 = 0;
let score2 = 200;

const defaultScore = 0;

function outer() {
    if (true) {
        let score: number;
        score = 30;
    }

    for (let i = 0; i < 3; i++) {
        setTimeout(() => {
            console.log(i); //0 1 2를 예상했겠지만 Nope! (3,3,3이 출력된다.)
        }, 100);
    }

    // console.log(score); //var로 if문에서 할당했다면, 할당한 0이 출력된다. (같은 함수 scope에 있기 때문) //let으로 할당했다면 block스코프 if안에서만 쓸수 있다.
}

outer();
