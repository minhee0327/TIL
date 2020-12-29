// 문제이해가 오래결린 문제.
// 논문인용횟수만큼 h값을 증가시켜가면서, h값보다 작은 값들과, 큰값들의 길이를 구했다.
// 각각의 값은 몇번 인용됬는지 값이고, 해당 값이 h와 비교했을때 아래 조건과 일치하면 ans를 업데이트 하는방향으로 풀었다.
function solution(citations) {
  let ans = 0;
  //   citations.sort((a, b) => a - b);
  for (let h = 0; h <= citations.length; h++) {
    less_h = citations.filter((x) => x <= h).length;
    gr_h = citations.filter((x) => x >= h).length;
    if (less_h <= h && gr_h >= h) {
      ans = h;
    }
  }
  return ans;
}

//간단해서 참조한코드
//1. 내림차 정렬
//2. 인덱스값과, 내림차 정렬된 위치의 값과 비교해서 인덱스값이 작거나 같으면 증가시켜나감.
function solution2(citations) {
  citations = citations.sort((a, b) => b - a);
  var i = 0;
  while (i + 1 <= citations[i]) {
    console.log(citations[i], i);
    i++;
  }
  return i;
}

console.log(solution([3, 0, 6, 1, 5]));
