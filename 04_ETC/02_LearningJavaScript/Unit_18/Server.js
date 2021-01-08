const http = require('http');

const server = http.createServer(function (req, res) {
    res.setHeader('Content-Type', 'application/json');

    //CORS 체크 비활성화
    //Ajax를 사용하면서 CORS 취약점이 드러났는데, 클라이언트(브라우저)가 보안 경고 출력하지 않도록함.
    //Access-Control-Allow-Origin header에 '*'값을 사용
    //실무에서는 이렇게 하면 안되고, 기본적으로 허용되는 같은 [프로토콜, 도메인, 포트]를 사용하거나
    //서비스에 접속할 수 있는 [프로토콜, 도메인, 포트]를 명시해야한다.!!!!
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.end(
        JSON.stringify({
            platform: process.platform,
            nodeVersion: process.version,
            uptime: Math.round(process.uptime()),
        }),
    );
});

const port = 7070;
server.listen(port, function () {
    console.log(`Ajax server strted on port ${port}`);
});
