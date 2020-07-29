function solution(array, commands) {
  return commands.map((command) => {
    // command를 비구조할당으로 시작점, 끝점, 출력위치값을 사용할수있음.
    const [start, end, ans] = command;
    // 새로운배열 (자르고, 정렬한후 해당 위치값을 뽑기)
    const newArray = array.slice(start - 1, end).sort((a, b) => a - b)[ans - 1];
    return newArray;
  });
}
