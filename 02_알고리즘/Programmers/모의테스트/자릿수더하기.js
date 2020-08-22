function solution(n)
{
    return n.toString().split('').reduce((a, c)=> a+parseInt(c),0)
}