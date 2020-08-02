function solution5(birth, current) {
  let birthArr = birth.toString().split(" ");
  let currentArr = current.toString().split(" ");

  let yearGap = parseInt(currentArr[3]) - parseInt(birthArr[3]);
  let MonthGap = current.getMonth() - birth.getMonth();
  let DateGap = current.getDate() - birth.getDate();
  let koreanAge = yearGap + 1;

  let man = -2;

  if (MonthGap > 0) {
    man += 1;
  } else if (MonthGap == 0) {
    if (DateGap > 0) {
      man += 1;
    }
  }
  man += koreanAge;

  return "만 " + man + "세, " + "한국나이 " + koreanAge + "세";
}

//test case

let birthday = new Date("December 27, 1993 00:00:00");
let currentDay = new Date("August 31, 2020 00:00:00");
console.log(solution5(birthday, currentDay));

birthday = new Date("August 08, 1993 00:00:00");
currentDay = new Date("August 31, 2020 00:00:00");
console.log(solution5(birthday, currentDay));

birthday = new Date("August 08, 1993 00:00:00");
currentDay = new Date("August 01, 2020 00:00:00");
console.log(solution5(birthday, currentDay));

birthday = new Date("August 08, 1993 00:00:00");
currentDay = new Date("Decenber 01, 2020 00:00:00");
console.log(solution5(birthday, currentDay));
