// if => ? 
function checkAge(age) {
    return (age > 18) ? true : confirm('보호자의 동의를 받으셨나요?');
}
// if => ||
function checkAge(age) {
    return (age > 18) || confirm('보호자의 동의를 받으셨나요?')
}


alert(checkAge(18) ? '네' : '아니요');