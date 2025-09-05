from concurrent.futures import ProcessPoolExecutor
import time

def pri(number):
    time.sleep(2)
    return f"Square :{number*number}"
numbers=[1,2,3,4,5,6,7,8,9,10]
if __name__ == "__main__":
    timer_start=time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(pri,numbers)
    for result in results:
        print(result)
    timer_end=time.time()-timer_start
    print(f"Total time taken is {timer_end} seconds")