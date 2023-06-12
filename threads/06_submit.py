import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def thread_kernel(thread_index):
    logging.info("I am thread %s", thread_index)
    time.sleep(2)
    logging.info("I am thread %s, and I am done", thread_index)
    str1 = "I am thread "+ str(thread_index)
    return str1

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S") 

    thread_index = [1, 2, 3]
    
    # create an instance of ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=8)
    
    # submit the tasks to the threadpool
    future = pool.submit(thread_kernel, 1) # this does not block
    
    result = future.result() # this blocks
    
    print(result)
    
    pool.shutdown()