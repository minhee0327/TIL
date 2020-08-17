try {
  console.log("this line is executed...");
  //   throw new Error("whoops");
  console.log("this line is not...");
} catch (e) {
  console.log("there was an error");
} finally {
  console.log("...always executed");
  console.log("perform cleanup here");
}

/* try쪽에 throw로 Error를 발생시킨 유무와 관계없이, 반드시 finally구문은 실행이 됨 */
