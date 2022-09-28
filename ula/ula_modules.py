#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():

        s = a ^ b 
        c = a & b
        
        soma.next = s
        carry.next = c
        

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    t1 = Signal(bool(0))
    t2 = Signal(bool(0))
    t3 = Signal(bool(0))
    h1 = halfAdder(a, b, t2, t1)
    h2 = halfAdder(c, t2, soma, t3)
    
    @always_comb   
    def comb():
        carry.next =   t1 | t3

        
    return instances()


@block
def adder2bits(x, y, soma, carry):
    c_out = Signal(bool(0))

    h1 = halfAdder(x[0],y[0],soma[0],c_out)
    h2 = fullAdder(x[1],y[1],c_out,soma[1],carry)

    return instances()



@block
def adder(x, y, soma, carry):        

    @always_comb
    def comb():
        sum = x+y
        soma.next = sum
        if sum > x.max -1:
            carry.next = 1
        else:
            carry.next = 0
        



    return instances()
