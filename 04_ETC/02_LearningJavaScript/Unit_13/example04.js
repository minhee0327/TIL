//함수에 별명붙이기
function addThreeSquareAddFiveTakeSqureRoot(x) {
  return Math.sqrt(Math.pow(x + 3, 2) + 5);
}
//위 함수를 별칭 f로 사용. 괄호를 붙이면 호출한다는 의미니까 붙이지 않도록 한다
const f = addThreeSquareAddFiveTakeSqureRoot;
const ans = (f(5) + f(2)) / f(7);
console.log(ans);

//node에서 별칭붙이는 예
/*
const Money = require("math-money"); //math-money라이브러리 불러와서 Money에 저장
const oneDollar = Money.Dollar(1);
const Dollar = Money.Dollar; //Money.Dollar 함수를 Dallar별칭으로 저장
const twoDollar = Money.Dollar(2);
*/
