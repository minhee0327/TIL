//블럭
{
    const name = 'minhee';
    console.log(name)
}
//console.log(name) // error 

//밖에서 안으로
let age = 29;
const name1 = 'minhee2';
{
    age++;
    console.log(age, name1);
}
console.log(age, name1)


//중첩
{
    {
        { console.log(age) };
    }
}