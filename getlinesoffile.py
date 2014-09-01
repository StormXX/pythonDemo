# -*- coding: utf-8 -*-

import time

file_name="test.c"

#count the func run time
def gettime(fun, n=10):
    start = time.clock()
    for i in range(n): fun()
    stend = time.clock()
    thetime = stend-start
    return fun.__name__, thetime

def getlines_one():
    return len(open(file_name).readlines())

def getlines_two():
    f=open(file_name)
    count=0
    for line in f:
        count+=1
    return count

def getlines_three():
    f=open(file_name)
    count=0
    for line in f.readlines():
        count+=1
    return count

def getlines_four():
    f=open(file_name)
    count=0
    while 1:
        buffer=f.read(65533)
        if not buffer:break
        count+=buffer.count('\n')
    return count


fun_list=[getlines_one,getlines_two,getlines_three,getlines_four]

for f in fun_list:
    print f.__name__,f()

for f in fun_list:
    print '%s,%.7f' % gettime(f)

