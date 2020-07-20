#!/bin/bash

daemons=("hello" "this" "is" "array")

echo ${daemons[1]} # daemons 배열의 두번째 인덱스, this 출력
echo ${daemons[@]} # daemons 배열 전체 출력
echo ${daemons[*]} # daemons 배열 전체 출력
echo ${#daemons[@]} # 전체 배열 크기

filelist=($(ls)) # 해당 쉘스크립트 실행 디렉토리의 파일리스트 변수할당
echo ${filelist[*]} #filelist 배열 모두 출력


