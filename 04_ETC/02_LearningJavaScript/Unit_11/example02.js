const email = null; //email이 문자열이 아닌 다른 값이 들어온 경우

function validateEmail(email) {
  return email.match(/@/) ? email : new Error(`invalid email: ${email}`);
}

try {
  const validatedEmail = validateEmail(email);
  if (validatedEmail instanceof Error) {
    console.error(`Error: ${validatedEmail.message}`);
  } else {
    console.log(`Valid email: ${validatedEmail}`);
  }
} catch (err) {
  console.log(`Error: ${err.message}`);
}

//Error: Cannot read property 'match' of null
//Cuase: null에는 match라는 프로퍼티를 읽을수 없게 되어 프로그램을 실행시켰지만
//예외상황을 캣치하여 어떤 에러상황인지 message프로퍼티로 확인할 수 있다.
