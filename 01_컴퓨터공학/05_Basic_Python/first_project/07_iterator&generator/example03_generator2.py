import time

def lazy_evaluation(n):
    print("1 sec sleep")
    time.sleep(1)
    return n

n_list = [lazy_evaluation((n))for n in range(1, 5+1)]
for i in n_list:
    print(i)

n_generator = (lazy_evaluation(n) for n in range(1, 5+1))
for i in n_generator:
    print(i)