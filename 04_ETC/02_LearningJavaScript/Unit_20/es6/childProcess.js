// exec => shell호출
const exec = require('child_process').exec;

// ls의 별칭 dir
// 호출되는 call stack은 Buffer객체 두개(stdout, stderr)받음 //옵션을 더 받을 수도있음(공식문서 참조)
exec('dir', function (err, stdout, stderr) {
    if (err) return console.error("Error executing 'dir'");
    stdout = stdout.toString() //Buffer => string
    console.log(stdout);
    stderr = stderr.toString();
    if (stderr !== '') {
        console.log('error:');
        console.log('stderr')
    }
})