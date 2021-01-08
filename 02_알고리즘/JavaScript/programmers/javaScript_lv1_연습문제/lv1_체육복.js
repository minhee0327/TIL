function solution(n, lost, reserve) {
  var sd = Array(n).fill(1);
  sd = [0].concat(sd);
  var lost = lost.sort();
  var reserve = reserve.sort();

  for (let i = 1; i <= n; i++) {
    if (reserve.includes(i)) {
      sd[i]++;
    }
    if (lost.includes(i)) {
      sd[i]--;
    }
  }

  for (let i = 1; i <= sd.length; i++) {
    if (sd[i] === 0 && sd[i - 1] === 2) {
      sd[i] += 1;
      sd[i - 1] -= 1;
    } else if (sd[i] === 0 && sd[i + 1] === 2) {
      sd[i] += 1;
      sd[i + 1] -= 1;
    }
  }

  return sd.filter((i) => i > 0).length;
}

console.log(solution(5, [2, 4], [3, 1, 5]));
console.log(solution(5, [2, 4], [3]));
console.log(solution(3, [3], [1]));

/*
[내가 짤 코드 순서]
- N만큼 크기의 배열 원소를 모두 1로 채운다.
- lost idx - 1 의 원소를 -1 해준다.
- 반복문 돌면서, reserve 원소에 해당하는 인덱스를 +1해준다.
- 반목문 돌면서, 2인 친구가 있고, 양 옆에 0인친구가 있으면 한벌 나눠준다.
- 배열의 값이 1 이상인 애들만 카운트한다.

[애먹은 위치]
- lost와 reverse된 값을 찾기 위해 마지막 반복문을 돌릴때, 해당 index를 어떻게 사용할지 고민을 많이함.
- 일단 맨앞에 0이라는 빈값을 넣어두고
- 1번 위치부터 반복하면서 0,2 인 경우와 2,0인 경우로 나누어서 생각! 

*/
