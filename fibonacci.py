#!/usr/bin/env python3

# Lab 16: recursion
# Fibonacci with cache
fact_cache = {}

def factorials(n):
    if n==0:
        return 1
    elif n in fact_cache:
        return fact_cache.get(n)
    else:
        x = n*factorials(n-1)
        fact_cache[n] = x
        return x

print(factorials(600))

