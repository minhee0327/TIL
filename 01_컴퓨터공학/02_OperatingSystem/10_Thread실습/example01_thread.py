import threading

g_count = 0


def thread_main():
    global g_count
    for i in range(10000):
        g_count = g_count+1


threads = []

for _ in range(50):
    th = threading.Thread(target=thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_count=', g_count)
# 결과가 50 * 10000
# thread_main의 값을 증가하면(예:1000000)
# 스레드가 온전히 1000000반복되지 않고, 다른 스레드로 context switching이 일어남
# 어느 부분을 실행하다가 context switching할지 알수 없으므로
# 원하는 결과가 나오지 않을 수 있다.
