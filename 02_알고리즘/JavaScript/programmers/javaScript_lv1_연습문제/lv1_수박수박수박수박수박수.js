function solution(n) {
  var answer = "";

  for (var i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      answer += "박";
    } else {
      answer += "수";
    }
  }

  return answer;
}

/**
 * javaScript에서 repeat()이라는 함수가 있다.
 * 이걸 사용하면 반복을 줄이고 코드를 작성할수있다.
 */
