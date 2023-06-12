import time
import nvtx


def sleep_for(i):
    time.sleep(i)

@nvtx.annotate()
def my_func():
    time.sleep(1)

with nvtx.annotate("for_loop", color="green"):
    for i in range(5):
        sleep_for(i)
        my_func()
