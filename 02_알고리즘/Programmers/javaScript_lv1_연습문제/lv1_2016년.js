function solution(a, b) {
  var answer = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
  //윤년은 2월이 29일까지
  var month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  //각 달까지의 누적 날짜
  var arr = [];

  for (var i = 0; i < 12; i++) {
    var ans = 0;
    for (var j = 0; j < i; j++) {
      ans += month[j];
    }
    arr.push(ans);
  }
  var date = (arr[a - 1] + b) % 7;
  return answer[date];
}

/* 예전에 SW expert에서 푼 문제랑 유사 (python으로 풀었던) */
/* 조금 더 javascript스러운 표현은 new Date() 객체사용 혹은 reduce를 사용해서 쉽게 구현가능하단점..!*/

function solutions2(a, b) {
  var date = new Date(2016, a - 1, b);
  //2016-05-23T15:00:00.000Z,Tue May 24 2016 00:00:00 GMT+0900 (대한민국 표준시)
  //   console.log(date, date.toString());
  return date.toString().slice(0, 3).toUpperCase();
}

console.log(solutions2(5, 24));

function solution3(a, b) {
  var answer = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  var month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  var date;
  if (a === 1) {
    date = b - 1;
  } else {
    date = month.slice(0, a - 1).reduce((a, b) => a + b) + b - 1;
  }

  return answer[date % 7];
}

console.log(solution3(5, 24));

/* reduce함수를 활용해서 누적값을 구하는 방법을 활용하기!! */
