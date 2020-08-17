// const err = new Error("invalid Email");

function validateEmail(email) {
  return email.match(/@/) ? email : new Error(`invalid email: ${email}`);
}

//instance of 연산자를 사용하여 Error 인스턴스가 반환하는지 여부 check
const email = "minhee@gmail.com";
const validatedEmail = validateEmail(email);

if (validatedEmail instanceof Error) {
  console.error(`Error : ${validatedEmail.message}`);
} else {
  console.log(`Valid email: ${validatedEmail}`);
}
