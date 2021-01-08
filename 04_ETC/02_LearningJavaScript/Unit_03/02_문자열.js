// escape 예시
const dialog = 'Sam looked up and said "don\'t do that!" to Max';
console.log("Windows line 1\r\nWindows line 2");

// template문자열
let currentTemp = 19.5;
const message = `The current temperature is ${currentTemp} \u00b0C`;
console.log(message);

const multiline = `line1
line2`;
console.log(multiline);

const multiline1 = "line1\n" + "line2\n" + "line3";
console.log(multiline1);

const multiline2 =
  "Current temperature: \n" +
  `\t${currentTemp}\u00b0C` +
  "Don't worry .. the heat is on!";
console.log(multiline2);
