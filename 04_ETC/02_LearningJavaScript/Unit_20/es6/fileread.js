const fs = require('fs');
const path = require('path');

fs.readFile(path.join(__dirname, '/fs/', 'hello.txt'), {
    encoding: 'utf8',
}, function (err, data) {
    if (err) return console.error(`Error reading File. ㅠ^ㅠ`);
    console.log(`Read file contents: `, data);
    //결과: Read file contents:  <Buffer 68 65 6c 6c 6f 20 66 72 6f 6d 20 4e 6f 64 65 7e>
})