const logInput = input => `입력한 값: ${input}`;
const logResult = (figure, result) => `${figure}의 넓이는 ${result} 입니다.` ;
const logFigureError =  "지원이 되지 않는 도형입니다. '정사각형' 혹은 '원' 을 입력해주세요. \n커맨드 라인 종료합니다..."

module.exports ={
    logInput,
    logResult,
    logFigureError
}