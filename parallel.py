#!/usr/bin/env python

import os, sys, errno
import re
import argparse
from time import time
import multiprocessing

import numpy as np
import matplotlib.pyplot as plt
import time

def sumuptoN(dummy,integer):
    sum = 0
    for i in range(integer+1):
        sum +=i
    return sum


if __name__ == '__main__':
    # Handle command line options
    parser = argparse.ArgumentParser(description='Plot random data in parallel')
    parser.add_argument('-o', '--outputDir', required=True,
                        help='The directory to which plot files should be saved')
    parser.add_argument('-n', '--number', required=False, type=int,
                        default=32,
                        help='The number of plots to make')
    parser.add_argument('--numProcessors', required=False, type=int,
                        default=multiprocessing.cpu_count(),
                        help='Number of processors to use. ' + \
                             "Default for this machine is %d" % (
                             multiprocessing.cpu_count(),))
    args = parser.parse_args()

    if not os.path.isdir(args.outputDir) or not os.access(args.outputDir,
                                                          os.W_OK):
        sys.exit("Unable to write to output directory %s" % (args.outputDir,))

    if args.number < 1:
        sys.exit('Number  must be greater than 0')

    if args.numProcessors < 1:
        sys.exit('Number of processors to use must be greater than 0')

    # Start my pool
    pool = multiprocessing.Pool(args.numProcessors)

    print("Find the sum of natural number upto a given number %d using %d processors..." %
          (args.number, args.numProcessors))

    # Build task list
    tasks = []
    number = 0
    while  number < args.number:
        number += 1
        tasks.append((args.outputDir, number))
    start = time.time()
    # Run tasks
    results = [pool.apply_async(sumuptoN, t) for t in tasks]
    # Process results
    for result in results:
        sum = result.get()
    print('The sum is', sum)
        #print("Result: sum is %d " % sum)
    end = time.time()

    print('execution time', end-start)
    
    pool.close()
    pool.join()
    start = time.time()
    for i in range(1,args.number+1):
        sum = sumuptoN(args.outputDir,i)
        #print('Sum is',sumuptoN(args.outputDir,i) )
    print('The sum is', sum)
    end = time.time()
    print('execution time', end-start)
