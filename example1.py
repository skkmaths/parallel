# SuperFastPython.com
# example of issuing a task with apply_async() to the process pool
from time import sleep
from multiprocessing.pool import Pool
# task executed in a worker process
def task():
    # report a message
    print(f'Task executing', flush=True)
    # block for a moment
    sleep(1)
# report a message
    print(f'Task done', flush=True)

# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    pool = Pool()
    # issue tasks to the process pool
    pool.apply_async(task)
    # close the process pool
    pool.close()
    # wait for all tasks to finish
    pool.join()