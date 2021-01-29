# System Structure

![image-20210129222438048](https://github.com/minhee0327/TIL/blob/master/image/c1.png)

* **CPU** 
  * 메모리로부터 매 클럭 사이클마다 명령(instruction)을 한 줄씩 읽어 실행 
  * **register**
    * CPU안에 메모리보다 더 빠르면서, 정보를 저장할 수 있는 공간.
    * 대표 register : Program Counter(pc)
  * **mode bit**
    * 운영체제인지, 사용자프로그램인지 구분을 해주는 bit 
    * 사용자 프로그램의 잘못된 수행으로, 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호장치.
    * 하드웨어(HW, 이하 HW) 적으로 두가지 모드의 operation지원
      * **1: 사용자모드** 
        * 사용자 프로그램 수행
        * 제한된 instruction만 수행. (보안에 따라)
        * 커널모드를 수행중이다가, 사용자 프로그램에게 CPU를 넘기기 전에 mode bit를 0으로 변경.
      * **0: 커널모드 (=모니터모드, 시스템모드)**
        * OS 코드 수행 
        * 보안을 해칠 수 있는 중요한 명령어는 커널 모드에서만 수행이 가능한 '특권 명령'으로 규정한다. 
        * 메모리 접근 뿐만이 아니라, I/O 디바이스 접근 혹은 모든 instruction을 수행할 수 있다.
        * 인터럽트나 예외상황에서 하드웨어가 mode bit를 0으로 변경.
  * **interrupt line (interrupt request line)**
    * I/O 디바이스에서 발생한 이벤트(인터럽트)를 알려줄 때 사용되는 장치. 
      * 예: 키보드 입력이 끝났거나, 디스크에서 읽어오는 작업이 끝났음을 알릴때 등
    * CPU는 하나의 insturction을 수행한 후, interrupt line을 확인하여 interrupt가 발생는지 확인하고, 발생 시, 현재 pc 주소를 읽어들이는 것이 아니라, 잠시 하던 작업을 멈추고 cpu를 누가 쓰고있었든 상관없이 제어권을 OS로 넘긴다. 
    * OS는 interrupt마다 상황에 맞게 처리해야하는 커널 함수로 정의된 인터럽트 벡터를 참조하여 인터럽트 처리하는 커널 함수를 수행한다. 
      * 인터럽트 벡터 = [인터럽트 번호: 인터럽트 처리주소(처리루틴, 핸들러)]



* **MEMORY**
  * CPU의 작업공간



* **DISK**
  * 파일에 저장, 읽어들이는 I/O측면



* **device controller**
  * 각 I/O 디바이스들은 디바이스를 전담하는 작은 cpu같은 것들이 붙어있는데 이를 device controller라고 한다.  (disk controller,  usb controller, graphic controller,...)
  * I/O 디바이스는 성능 (처리하는 속도) 이 많이 차이가 난다.
    * 예: Disk는 CPU에 비해 100만배 가량 느림. 
      따라서, CPU가 직접 Disk를 관장하는 것이 아니라, disk controller가 담당

* **local Buffer:**
  * 메인 CPU의 작업공간인 메모리가 있듯, 각 device controller의 작업공간.



* **timer**
  * 특정 프로그램이 CPU를 독점하는 것을 막기 위한 하드웨어 장치
  * 컴퓨터가 켜지면, OS가 CPU를 가지고 있다가 사용자 프로그램 실행시 timer에 값을 세팅한 후 CPU를 사용자 프로그램에게 넘겨준다. 이 때, 사용자 프로그램은 timer에 세팅한 시간이 다 되면, CPU로 interrupt를 걸어준다. (매 클럭 사이클마다 1씩 감소하면서 타이머 값이 0이 되면 타이머 인터럽트 발생)
  * time sharing(시분할)을 구현하기 위해 널리 사용됨.



* **DMA (Direct Memory Access)**
  * 원래는 CPU만 메모리에 접근했었는데, CPU에 독립적으로 직접 메모리에 접근할수 있게 됨.
  * 직접 메모리에 접근하는 컨트롤러.
  * I/O장치의 데이터는 device controller에 의해 local buffer로 이동한다.
    이 때 전송할 데이터가 많은 경우, 많은 양의 데이터를 memory로 copy하는 작업을 cpu가 하게 되면 오버헤드가 크다. 이를 보완하기 위해 생겼다. DMA로 데이터를 모두 copy(전송)한 후에 전송 완료된 인터럽트를 단 한번만 걸면 오버헤드가 감소한다.
  * local buffer의 특정 크기 (블럭 or page정도의 데이터)가 쌓이면, 그 때 cpu에 한번 interrupt를 걸어줌. 
    (DMA가 Memory에 내용을 copy해주고, 블럭 단위의 데이터가 쌓은 경우에만cpu에 알려주어 interrupt당하는 빈도를 줄여줌)
  * cpu의 중재 없이 device controller가 device의 buffer storage내용을 메모리에 block 단위로 직접 전송
  * byte단위가 아닌 block(혹은 page) 단위로 인터럽트 발생.
  
  
* **Memory Controller**
  
  * CPU와 DMA가 동시에 접근하지 못하도록 교통정리하는 역할 수행.





