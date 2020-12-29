process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);

  for (var l = 0; l < b; l++) {
    console.log("*".repeat(a));
  }
});

/*
//template 문자열로 진행

process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);

  const s = `${"*".repeat(a)}\n`;
  console.log(s.repeat(b));
});
*/
