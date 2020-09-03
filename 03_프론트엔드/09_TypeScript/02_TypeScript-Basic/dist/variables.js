var score1 = 0;
let score2 = 200;
const defaultScore = 0;
function outer() {
    if (true) {
        let score;
        score = 30;
    }
    for (let i = 0; i < 3; i++) {
        setTimeout(() => {
            console.log(i);
        }, 100);
    }
}
outer();
//# sourceMappingURL=variables.js.map