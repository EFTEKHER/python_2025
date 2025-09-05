from concurrent.futures import ThreadPoolExecutor
import time
import threading
def pri(number):
    time.sleep(2)
    return f"Number :{number} printed by thread : {threading.current_thread().name}"

nuymbers=[1,2,3,4,5,6,7,8,9,10]
timer_start=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(pri,nuymbers)
for result in results:
    print(result)
timer_end=time.time()-timer_start
print(f"Total time taken is {timer_end} seconds")    