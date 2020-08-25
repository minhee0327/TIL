/*
console.log("Before timeout: "+ new Date());

setTimeout(function(){
    console.log("After timeout: " + new Date());
}, 1000);

console.log("I happen after setTime out!")
console.log("Me too")
*/

const start = new Date();
let i = 0

const intervalId = setInterval(function(){
    let now = new Date();

    if(now.getMinutes() !== start.getMinutes() || i++> 10){
        return clearInterval(intervalId)
    }

    console.log(`${i} : ${now}`)

}, 5*1000)