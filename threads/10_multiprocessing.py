from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)

    start = time.time()

    # A process gets own Python interpreter and memory space.
    # So GIL is no loanger a problem
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])

    pool.close()
    pool.join()

    end = time.time()

    # Procceses are heavier than threads. 
    # So there is a high overhead in launcing them.
    print('Time taken in seconds -', end - start)