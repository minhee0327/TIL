function solution(s) {
  if (s.length === 4 || s.length === 6) {
    if (!isNaN(s * 1) && s.length === (s * 1 + "").length) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}

console.log(solution("a234"));
console.log(solution("1234"));

/*
- 문제를 잘 읽어봐야했던 문제 + 조건을 잘 체크할 문제
- 문자열 길이 4 혹은 6일때 
- 숫자인 경우 (+빈공백이 안주어졌을 경우에만 숫자임) 만 true
- 나머지는 false

- 처음에 NaN !== s*1 이런식으로 진행했는데, 이걸로는 s*1이 NaN인지 유무를 체크할 수 없었다.
- 그래서 찾아보니 isNaN()를 사용해서, NaN인지 유무를 체크하는 함수가 있었다.
- NaN는 숫자이기는 하지만, 컴퓨터가 처리할 수 없는 수이다. 따라서 비교연산자보다 함수를 사용해야했다.
*/
