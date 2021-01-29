# Computer Architecture 
### (aka 폰 노이만 구조, 컴퓨터 구조)

![image-20210129213604328](https://github.com/minhee0327/TIL/blob/master/image/c2.png)

* Processor(CPU)
  * 메모리로부터 데이터와 명령을 받음
  * 컴퓨터 명령어(기계어, instruction)을 해석하고 연산함. 인간의 두뇌역할
  * CU(Control Unit)은 프로그램 명령에 따라 데이터 패스, 메모리 입출력 동작 결정
  * ALU(Arithmetic Logic Unit): 산술 논리 연산장치
    * 사칙연산, 논리곱, 논리합, 부정합 등 논리연산 수행 필요한 데이터를 레지스터에서 가져오고, 다시 결과를 레지스터에 저장.
* Memory
  * 명령어 및 데이터 적재(Load)
  * 정보를 저장해 뒀다가 필요할 때 읽어들이는 장소
  * 레지스터의 용량이 작아 출시
    * 비휘발성 (ROM)
    * 휘발성(RAM)
    * 최근 사용 데이터 (Cache)

* Input(입력장치)
  * 데이터 입력위한 외부장치
  * 키보드, 마우스, 스캐너 등
* Output(출력장치)
  * 컴퓨터에서 처리 결과를 출력해주는 외부 장치