for (let temp, i = 0, j = 1; j < 30; temp = i, i = j, j = temp + i) {
  console.log(temp, i, j);
}

for (let i in "abcdefcg") {
  console.log(i);
}
