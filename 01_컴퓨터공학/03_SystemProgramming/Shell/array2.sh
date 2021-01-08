#!/bin/bash

daemons=("hello" "this" "is" "array")

echo $daemons[1] # 중괄호를 없애고 출력해봄
echo $daemons[@] # 중괄호를 없애고 출력해봄
echo ${daemons[*]} 
echo ${#daemons[@]}

filelist=($(ls)) 
echo ${filelist[*]} 


