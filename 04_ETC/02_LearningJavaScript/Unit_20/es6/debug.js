//함수 모듈을 통한 모듈 커스터마이징

let lastMessage;

module.exports = function (prefix) {
    return function (msg) {
        const now = Date.now();
        const sinceLastMessage = now - (lastMessage || now);
        console.log(`${prefix} ${msg} +${sinceLastMessage}ms`);
        lastMessage = now;
    }
}