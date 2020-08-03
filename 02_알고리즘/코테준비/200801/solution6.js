function solution5(current, event) {
  let timeGap = event.getTime() - current.getTime();

  let hourGap = Math.floor(
    (timeGap % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  let minutesGap = Math.floor((timeGap % (1000 * 60 * 60)) / (1000 * 60));
  let secondsGap = Math.floor((timeGap % (1000 * 60)) / 1000);
  let dateGap = parseInt(timeGap / (24 * 60 * 60 * 1000));
  console.log(dateGap, hourGap, minutesGap, secondsGap);

  let ResultGap = [dateGap, hourGap, minutesGap, secondsGap];
  let words = ["일", "시", "분", "초"];
  let idx = 0;

  // 1로 시작하는 위치를 찾기위한 반복문
  for (let i = 0; i < 4; i++) {
    if (ResultGap[i] === 1) break;
    idx += 1;
  }

  //0일 1시 1분 1초일 경우 0을 제외한 결과값 만들기위한 반복문
  let ans = "";
  for (let i = idx; i < ResultGap.length; i++) {
    ans += ResultGap[i] + words[idx];
    idx++;
  }

  return ans;
}

let currentDate = new Date("August 29, 2020 22:58:59");
let eventDate = new Date("August 31, 2020 00:00:00");
console.log(solution5(currentDate, eventDate));

currentDate = new Date("August 30, 2020 23:58:59");
eventDate = new Date("August 31, 2020 00:00:00");
console.log(solution5(currentDate, eventDate));

currentDate = new Date("August 30, 2020 23:00:00");
eventDate = new Date("August 31, 2020 00:00:00");
console.log(solution5(currentDate, eventDate));
