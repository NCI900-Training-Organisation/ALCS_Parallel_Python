import time
from threading import Thread
import sys

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

# Python manages a memory using reference counting
a = []
b = a
print('Refcount = ', sys.getrefcount(a)) 

# Reference count variable needed protection from race conditions 
# The GIL is a single lock on the interpreter itself.
# Any execution Python bytecode requires acquiring the interpreter lock.
# So in a CPU bound problem, the threads are serialized.
