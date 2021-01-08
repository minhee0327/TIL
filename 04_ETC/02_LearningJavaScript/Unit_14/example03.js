// 노드에서 file 읽을때

const fs = require('fs');

const fname = 'blabla.txt';
fs.readFile(fname, function(err, data){
    if (err) return console.error(`error reading file ${fname}: err.message`);
    console.log(`${fname} contents: ${data}`);
})