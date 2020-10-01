let ask = (question, yes, no) => confirm(question) ? yes() : no();

ask("동의하십니까?", () => alert("동의함."), () => alert("동의 불가!"))