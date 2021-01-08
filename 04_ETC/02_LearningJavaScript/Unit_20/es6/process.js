const fs = require('fs');

/*
fs.readdir('data', function (err, files) {
    if (err) {
        console.error(`Fatal error: Couldn't read data dir`);
        process.exit(1);
    }
    const txtFiles = files.filter(f => /\.txt$/i.test(f));
    if (txtFiles.length === 0) {
        console.log("No .txt files to process");
    }
})*/
// console.log(process.argv)
const filenames = process.argv.slice(2);
let counts = filenames.map(f => {
    try {
        const data = fs.readFileSync(f, {
            encoding: 'utf8',
        })
        return `${f}: ${data.split('\n').length}`
    } catch (err) {
        return `${f}: couldn't read file `
    }
})

console.log(counts.join('\n'))