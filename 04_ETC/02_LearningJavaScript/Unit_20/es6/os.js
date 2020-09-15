// OS 정보를 읽을 수 있는 노드 모듈

const os = require('os');

console.log('Hostname: ' + os.hostname());
console.log('OS type: ' + os.type());
console.log('OS platform: ' + os.platform());
console.log('OS release: ' + os.release());
console.log('OS uptime: ' + (os.uptime() / 60 / 60 / 24).toFixed(1) + " days");
console.log('CPU architecture: ' + os.arch());
console.log('Number of CPUs: ' + os.cpus().length);
console.log('Total Memory: ' + (os.totalmem() / 1e6).toFixed(1) + " MB");
console.log('Free Memory: ' + (os.freemem() / 1e6).toFixed(1) + " MB");

/*
Hostname: LAPTOP-EJUG2DSO
OS type: Windows_NT
OS platform: win32
OS release: 10.0.18363
OS uptime: 1.2 days
CPU architecture: x64
Number of CPUs: 8
Total Memory: 8439.8 MB
Free Memory: 3593.3 MB
*/