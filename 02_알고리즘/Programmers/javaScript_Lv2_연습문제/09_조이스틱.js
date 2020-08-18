function solution(name) {
  const start = "A".charCodeAt(0);
  const end = "Z".charCodeAt(0) + 1;
  const strs = name.split("");
  let ans = 0;
  let i = 0;

  while (true) {
    // A가 아닌 곳을 A로 바꿔주되, A에서 가까운지, Z에서 가까운지 체크하고 작은값만큼 ans에 합해줌
    if (strs[i] !== "A") {
      const c = strs[i].charCodeAt(0);
      const down = Math.abs(start - c);
      const up = Math.abs(end - c);

      ans += Math.min(down, up);
      strs[i] = `A`;
    }
    // strs의 요소가 모두 A인 경우, -1을 반환한다.
    // 모두 A이니까 str!=='A'를 만족하는 값이 없기때문.
    // 이경우에는 name을 모두 순회해서 해당 값으로 변경했다는 것이기때문에 반복문을 종료한다.
    if (strs.findIndex((str) => str !== "A") === -1) {
      break;
    }

    let rightCnt = 0,
      rightIdx = 0,
      leftCnt = 0,
      leftIdx = 0;

    //오른쪽으로 카운트(A가 아닌위치까지)
    for (let r = 1; r < strs.length; r++) {
      rightIdx = (i + r) % strs.length;
      if (strs[rightIdx] !== "A") {
        rightCnt = r;
        break;
      }
    }
    // A가 아닌곳까지 카운트함
    for (let l = 1; l < strs.length; l++) {
      leftIdx = i - l < 0 ? i - l + strs.length : i - l;
      if (strs[leftIdx] !== "A") {
        leftCnt = l;
        break;
      }
    }

    // 좌, 우 값중 작은쪽으로 이동함.
    if (rightCnt <= leftCnt) {
      i = rightIdx;
      ans += rightCnt;
    } else {
      i = leftIdx;
      ans += leftCnt;
    }
  }
  console.log(ans);
  return ans;
}

solution("JEROEN");
solution("JAN");

/*
[Code Review]
- 2시간 이상 고민했는데, 어려워서 다른 분 코드를 참조했다.
- 나는 AAAA로 문자열을 먼저 name의 크기만큼 만들어서 , name을 만들 생각을 했는데
- 반대로 name을 AAAA..형태로 만들어가는 식으로 생각했다는 점이 인상깊다.

- z의 경우 거꾸로 세기때문에 +1을 해줘야한다는 사실도 망각했다.

- 또, 좌, 우 를 카운트해가면서 작은 값을 찾아 해당 인덱스로 건너뛰는 방법을 어떻게 구현해야할지가 고민이었는데 위 방법을 앞으로 활용해야겠다.

- 마지막으로 가장인상깊은 한줄은
findIndex를 통해서 모든 값이 'A'가 됬을 경우를 표현한 것이 새롭다. 
나라면 set을 사용해서 길이가 1이고, 값이 A인지를 체크해봤을 것 같다. (시간측면에서 효율적인지 의문)
*/
