## Process that run in parallel
## CPU Bound Tasks-Tasks that require significant CPU processing power, such as complex calculations or data processing. Multiprocessing can help distribute the workload across multiple CPU cores, improving performance.
## parallel execution-When you need to perform multiple tasks in parallel, such as running simulations or processing large datasets. Multiprocessing can help speed up the execution time by utilizing multiple CPU cores.

import multiprocessing
import time
def pri():
    for i in range(5):
        time.sleep(2)
        print(f"square is {i*i}\n")
def tri():
    for i in range(5):
        time.sleep(2)
        print(f"cube is {i*i*i}\n")

if __name__ == "__main__":
    t1 = multiprocessing.Process(target=pri)
    t2 = multiprocessing.Process(target=tri)
    t=time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    total=time.time()-t
    print(f"Total time taken is {total}")
