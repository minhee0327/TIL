// outer variable(global variable), project전체에서 사용되는 변수가 아니라면 자제
let userName = 'minhee'

function showMessage() {
    // local variable
    // outer variable 함수 내부에서 참조 및 수정가능
    let msg = 'hello '
    userName = 'Bob';
    alert(msg + userName);
}
// 호출 전이기 때문에 minhee
// alert(userName);

// local variable은 외부에서 참조 불가
showMessage();

//호출 후이기 때문에 bob
// alert(userName);