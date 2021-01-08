// 웹서버 요청
// 조금 더 쉽게 웹사이트 구현하고 싶다면 => express, Kora 프레임워크를 사용하면 처음부터 웹서버 구현하는 부담
const http = require('http');

const server = http.createServer(function (req, res) {
    if (req.method === 'GET' && req.url === '/favicon.ico') {
        const fs = require('fs');
        fs.createReadStream('favicon.ico');
        // fs.pipe(res);
        // fs.end(res);
    } else {
        console.log(`${req.method} ${req.url}`);
        res.end('Hello world');
    }
});

const port = 8080;
server.listen(port, function () {
    console.log(`server started on port ${port}`);
});