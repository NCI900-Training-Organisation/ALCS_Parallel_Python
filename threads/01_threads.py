import logging
import threading
import time

def thread_kernel(thread_index):
    logging.info("I am thread %s", thread_index)
    time.sleep(2)
    logging.info("I am thread %s, and I am done", thread_index)
 

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  

    # When creating a thread you have to pass the function the thread will execute and 
    # the arguments to that function.
    logging.info("Create thread")
    thread_1 = threading.Thread(target=thread_kernel, args=(1,))
    logging.info("Start thread")
    thread_1.start()
    logging.info("Thread execution complete")
    logging.info("Exiting.....")
