function solution(strings, n) {
  strings.sort(function (a, b) {
    if (a[n] > b[n]) return 1;
    if (a[n] < b[n]) return -1;
    if (a[n] === b[n]) return a.localeCompare(b);
  });
  return strings;
}

/*
- javascript의 배열은 python에서 단순히 sort()를 썼던 것과는 조금 다르다.
- 특히 앞의값, 뒤의값 (a,b)를 매개변수로 받아서
- 둘중에 앞에 값이 크면 return 1, 뒤의값이 크면 return -1을 해서 오름차 정렬이 가능하다.(내림차면 거꾸로하면됨)
- 오히려 JAVA창 비슷한 모양새라고 생각이 들었음...ㅠㅠ

- 여기서 한번더 생각을하게 만드는 코드가 있었으니.. 아래코드
*/

function solution1(strings, n) {
  return strings.sort((a, b) =>
    a[n] === b[n] ? (a > b) - (a < b) : (a[n] > b[n]) - (a[n] < b[n])
  );
}

console.log(solution1(["abce", "abcd", "cdx"], 2));
console.log(solution1(["sun", "bed", "car"], 1));

/*
- 두가지 방법을 떠올리면 좋을 듯하다.
1. a.localeCompare(b) : a>b면 1, a<b면 -1, a===b면 0을 반환하는 함수
2. (a>b) - (a<b): 만약 a>b면 1, a<b면 -1, a===b면 0이 되는 식
이걸 통해서 정렬을 할때, 내 구미에 맞게 정렬하기 수월해진다.

[뭐..아니면.... 정렬을 구현하는것도 하나의 방법이겠지..]

*/
