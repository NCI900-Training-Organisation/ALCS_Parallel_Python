import logging
import threading
import time

def thread_kernel(thread_thread_index):
    logging.info("I am thread %s", thread_thread_index)
    time.sleep(2)
    logging.info("I am thread %s, and I am done", thread_thread_index)
 

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  


    list_threads = list()
    for thread_index in range(3):
        logging.info("Create thread %d", thread_index)
        thread_x = threading.Thread(target=thread_kernel, args=(thread_index,))

        #append the thread handle to the list
        list_threads.append(thread_x)
        thread_x.start()

    for thread_index, thread_x in enumerate(list_threads):
        # wait for all the threads
        thread_x.join()
        logging.info("Join thread %d", thread_index)