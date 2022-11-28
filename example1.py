# SuperFastPython.com
# example of issuing a task with apply_async() to the process pool
from time import sleep
from multiprocessing.pool import Pool
from multiprocessing import Process
import numpy as np
import time
import multiprocessing
from joblib import Parallel, delayed
# task executed in a worker process
nc = 1000000000
u = np.zeros(nc)
v = np.zeros(nc)
def task(u,v):
    # report a message
    print(f'Task executing', flush=True)
    # block for a moment
    #sleep(1)
# report a message
    #print(f'Task done', flush=True)
    for i in range(0,nc):
        u[i] = 1.0
        v[i] = 1.0
    print('task executed')
    #return u
def out(u):
    #print('u=',u)
    return (u)
def task2(i):
    u[i] = 1.0
inputs = range(nc)
# protect the entry point
if __name__ == '__main__':

    # create and configure the process pool
    
    start = time.time()
    pool = Pool()
    #issue tasks to the process pool
    results = pool.apply_async(task, args=(u,v))
    
    #close the process pool
    pool.close()
    # wait for all tasks to finish
    pool.join()
    #print('result=',results.get())
    end = time.time()
    print('execution time = ', end-start)
    
    start = time.time()
    print(f'Task executing', flush=True)
    for i in range(0,nc):
        u[i] = 1.0
        v[i] = 1.0
    print('task executed')
    end = time.time()
    print('execution time = ', end-start)
    
    start = time.time()
    p = Process(target = task, args = (u,v))
    p.start()
    p.join()
    end = time.time()
    print('execution time = ', end-start)
    