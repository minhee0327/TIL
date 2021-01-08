/* reducer + 객체 예시 */
const animals = [
  "Dog",
  "Cat",
  "Lion",
  "Cow",
  "Sheep",
  "Cheetah",
  "Deer",
  "Goat",
  "Pig",
  "Panda",
  "Dolphin",
];
const test = animals.reduce((a, x) => {
  if (!a[x[0]]) a[x[0]] = [];
  a[x[0]].push(x);
  return a;
}, {});

console.log(test);
