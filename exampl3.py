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
nc = 10
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
    num_cores = multiprocessing.cpu_count()
    print('Number of processors = ', num_cores)
    results = Parallel(n_jobs=num_cores)(delayed(task2)(i) for i in inputs)
    print(u)