//아래 함수를 호출할때마다, colorIndex값이 수정이되고,(부수효과)
//호출할때마다 red, oragne, yellow,...이런식으로 값이 다 다름
//따라서 순수한 함수라고 할 수 없음
const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
let colorIndex = -1;

function getNextRainbowColor() {
  if (++colorIndex >= colors.length) colorIndex = 0;
  return colors[colorIndex];
}

// 아래 순수한 함수 예제
// 입력이 같으면, 결과가 항상 같고 부수효과가 없기 때문
function isLeapYear(year) {
  if (year % 4 !== 0) return false;
  else if (year % 100 !== 0) return true;
  else if (year % 400 != 0) return false;
  else return true;
}

//만약 getNextRaninbowColor를 순수한 함수로 만들고싶다면 이터레이터를 사용
function getRaninbowIterator() {
  const rainbows = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
  ];
  let colorIdx = -1;
  return {
    next() {
      if (++colorIndex >= rainbows.length) colorIdx = 0;
      return { value: rainbows[colorIdx], done: false };
    },
  };
}
const rainbowIterator = getRaninbowIterator();
setInterval(function () {
  document.querySelector(".rainbow").style[
    "background-color"
  ] = rainbowIterator.next().value;
}, 500);
