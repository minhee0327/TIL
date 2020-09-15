const fs = require('fs');
const path = require('path');


fs.writeFile(path.join(__dirname, "/fs/", 'hello.txt'), 'hello from Node~',
    function (err) {
        if (err) console.log(`Error writing to file.`)
    })