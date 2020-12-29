function solution(N, stages) {
  var answer = [];
  var countArr = Array(N + 1);

  ArrayDefaltZero(countArr);

  for (var i of stages) {
    countArr[i - 1] += 1;
  }

  var people = countArr.reduce((a, c) => a + c);
  var loseratio = [];

  for (var i = 0; i < countArr.length - 1; i++) {
    loseratio.push({
      stage: i + 1,
      rate: countArr[i] === 0 || people === 0 ? 0 : countArr[i] / people,
    });
    people -= countArr[i];
  }

  loseratio.sort((a, b) =>
    a.rate === b.rate ? a.stage - b.stage : b.rate - a.rate
  );

  for (let i = 0; i < loseratio.length; i++) {
    answer.push(loseratio[i].stage);
  }

  return answer;
}

function ArrayDefaltZero(lst) {
  for (var i = 0; i < lst.length; i++) {
    lst[i] = 0;
  }
  return lst;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
