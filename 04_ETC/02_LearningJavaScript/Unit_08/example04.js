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

/*filter + join예시 */
const longWords = animals.filter((x) => x.length >= 5).join(" ");
console.log(longWords);

/*reducer 예시*/
const longWords2 = animals
  .reduce((a, c) => (c.length >= 5 ? a + " " + c : a), "")
  .trim();
console.log(longWords2);
