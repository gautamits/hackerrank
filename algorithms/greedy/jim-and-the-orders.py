#!/bin/python

import sys

def jimOrders(orders):
    # Complete this function
    serial=[]
    time=[]
    for i in range(len(orders)):
        serial.append(i+1)
        time.append(orders[i][0]+orders[i][1])
    time,serial=zip(*sorted(zip(time,serial)))
    return serial
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    orders = []
    for orders_i in xrange(n):
        orders_temp = map(int,raw_input().strip().split(' '))
        orders.append(orders_temp)
    result = jimOrders(orders)
    print " ".join(map(str, result))
