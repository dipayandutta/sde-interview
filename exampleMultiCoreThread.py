from multiprocessing import Process
import time

def cpu_task():
	total = 0
	for i in range(10_000_000):
		total +=i

processes = []
start = time.time()

for _ in range(4):
	p = Process(target=cpu_task)
	processes.append(p)
	p.start()

for p in processes:
	p.join()

print ("Time Taken: ",time.time()-start)
