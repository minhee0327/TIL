// s: seconds
function countdown(s){
    return new Promise (function (resolve, reject){
        for(let i = s; i>= 0; i--){
            setTimeout(function(){
                //에러 발생 (test 용)
                if( i === 13) return reject(new Error('Oh my GOD!'))

                if (i>0) console.log(i + "...");
                else resolve(console.log("GO!"))
            }, (s-i)*1000)
        }
    })
}



// 반환된 promise를 then 핸들러로 바로 호출
// then 핸들러는 성공콜백과, error 콜백을 받음 (항상 2가지만 받음) 
/*
countdown(5).then(
    function(){
        console.log("countdown completed successfully");
    },
    function(err){
        console.log("countdown experienced an error: " + err.message);
    }
)
*/

// promise는 catch 핸들러도 지원이 됨. 
const p = countdown(14)

p.then(
    function(){
        console.log("countdown completed successfully");
    }
)

p.catch(
    function(){
        console.log("countdown experienced an error: " + err.message)
    }
)