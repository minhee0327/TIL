import threading

g_count = 0


def thread_main():
    global g_count
    lock.acquire()  # 2
    for _ in range(10000):
        g_count = g_count+1
    lock.release()  # 3


lock = threading.Lock()  # 1
threads = []

for i in range(50):
    th = threading.Thread(target=thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_count=', g_count)

'''
1. 동기화 이슈 (example01):데이터를 공유하고 순서없이 읽고 쓰면서 원치 않는 결과가 나옴
2. 동기화 이슈가 발생한 영역을 한방에 실행할 수 있다면 문제 해결됨 
3. 임계자원을 처리하는 핵심 코드를 임계영역이라 하는데, 이 영역을 (#2~#3사이)
한번에 한 스레드만 사용할 수 있게끔 하면 해결됨
4. 임계영역에 들어가기전에 lock.aquire()를 해두면, 열쇄를 가지고 있는것과 동일. 이 열쇄를 가진 스레드만 동작할 수 있음.
5. 다 실행하고나면 lock.release()를 해줌으로써 열쇄를 반환하고 다른 스레드들도 정상 동작 가능해짐.
6. 이를 mutual exclusion이라고 하고, 결과적으로 원하는 결과를 얻을 수 있게 됨.
'''
