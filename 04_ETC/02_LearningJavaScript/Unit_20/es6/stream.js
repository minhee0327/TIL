// stream 형태 데이터를 다루는 객체
// 읽기, 쓰기, 이중 stream
// 예: 사용자의 타이핑 or 클라이언트와 서버 통신
// file 작업을 스트림으로 하는 예시를 연습해보자.

const fs = require('fs');
const path = require('path');

const ws = fs.createWriteStream(path.join(__dirname, '/fs/', 'stream.txt'), {
    encoding: 'utf-8',
});
ws.write('line 1 \n');
ws.write('line 2 \n');
ws.end();

const rs = fs.createReadStream(path.join(__dirname, '/fs/', 'stream.txt'), {
    encoding: 'utf-8',
});
rs.on('data', function (data) {
    console.log('>> data: ' + data + data.repeat('\n', '\\n'));
});
rs.on('end', function (data) {
    console.log('>> end');
});
