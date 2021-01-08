const { clear } = require('console');

const EventEmitter = require('events').EventEmitter;

class Countdown extends EventEmitter{
    constructor(s, superstitious){
        super();
        this.s = s;
        this.superstitious = !!superstitious;
    }

    go(){
        const countdown = this;
        const timeoutIds = [];
        return new Promise (function (resolve, reject){
            for(let i = countdown.s; i>= 0; i--){
                timeoutIds.push(setTimeout(function(){
                    if(countdown.superstitious && i === 13) {
                        //만약 위 i 값이 13이라면, timeoutIds배열에 담았던 callback함수들을 clear해줌으로서 동작X
                        timeoutIds.forEach(clearTimeout)
                        return reject(new Error('Oh my GOD!'))
                    }
                    //emit method: 등록한 이벤트를 호출할 수 있다.
                    countdown.emit('tick', i)
                    
                    if(i === 0) resolve();
                }, (countdown.s-i)*1000))
            }
        })
    }
}

function launch(){
    return new Promise(function(resolve, reject){
        if (Math.random < 0.5 ) return ; //결정되지 않는 프로미스 방지하는 코드 (5/10의 확률로 실패)
        console.log("Lift off");
        setTimeout(function(){
            resolve("In orbit!")
        }, 2*1000);
    })
}

function addTimeOut(fn, timeout){
    if(timeout === undefined) timeout = 1000;
    return function(...args){
        return new Promise(function(resolve, reject){
            const tid = setTimeout(reject, timeout, new Error("promise timed out"));
            fn(...args)
                .then(function(...args){
                    clearTimeout(tid);
                    resolve(...args);
                })
                .catch(function(...args){
                    clearTimeout(tid);
                    reject(...args)
                })
        })
    }
}

const c =new Countdown(11, true)

//eventEmitter.on(): 리스너를 등록
c.on('tick', function(i){
    if(i>0) console.log(i + '...')
})

c.go()
    .then(addTimeOut(launch, 11*1000))
    .then(function(msg){ console.log(msg)})
    .catch(function(err){
        console.error(err.message)
    })



