import logging
import threading
import time
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def thread_kernel_add(thread_index, repeat, value):
    logging.info("I am thread %s", thread_index)

    global sum # modify the scope of the variable
    logging.info("Initial sum in thread %s : %d", thread_index, sum)
   
    for i in range(repeat):
        tmp = sum
        sleep(0)
        tmp = tmp + value
        sleep(0)
        sum = tmp

    logging.info("Final sum in thread %s : %d", thread_index, sum)
    logging.info("I am thread %s, and I am done", thread_index)

def thread_kernel_sub(thread_index, repeat, value):
    logging.info("I am thread %s", thread_index)

    global sum # modify the scope of the variable
    logging.info("Initial sum in thread %s : %d", thread_index, sum)
    
    for i in range(repeat):
        tmp = sum
        sleep(0)
        tmp = tmp - value
        sleep(0)
        sum = tmp

    logging.info("Final sum in thread %s : %d", thread_index, sum)
    logging.info("I am thread %s, and I am done", thread_index)

if __name__ == "__main__":
 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  
    
    sum  = 0
    
    # launch the threads
    adder = threading.Thread(target=thread_kernel_add, args=(1, 1000000, 100) ) # adder threads
    adder.start()
    
    subtractor = threading.Thread(target=thread_kernel_sub, args=(2, 1000000, 100) ) # subtractor threads
    subtractor.start()
    
    adder.join()
    subtractor.join()
    
    print("Sum = "+ str(sum))
