// switch => if
let browser = prompt("what is your browser??", "");

if (browser === 'Edge') {
    alert('Edge를 사용하고 있습니다.')
} else if (browser === 'Chrome' || browser === 'Firefox' || browser === 'Safari' || browser == 'Opera') {
    alert('지원하고 있는 브라우저를 사용중입니다.')
} else {
    alert('현재 페이지가 잘 보이나요?')
}

// 일치연산자 (===), 동등연산자(==)
// 어차피 비교하려는 값이 문자열이니까, 동등연산자 사용해도 괜찮다.