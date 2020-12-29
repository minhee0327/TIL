function solution(seoul) {
  var answer = "";
  answer += "김서방은 " + seoul.indexOf("Kim") + "에 있다";
  return answer;
}

/**
 * 처음에 반복문으로 하나하나 접근하려고 하다가, 단순위치 반환이라면 index를 찾는 함수는 없을까하여
 * indexOf, includes, lastIndexOf를 찾아보게되었다.
 * 확실히 반복문보다 코드가 간결해서 좋았던 ㅎㅎ
 */
