import threading
import time

def cpu_task():
    total = 0
    for i in range(10_000_000):
        total += i

threads = []
start = time.time()

for _ in range(4):
    t = threading.Thread(target=cpu_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Time taken:", time.time() - start)

