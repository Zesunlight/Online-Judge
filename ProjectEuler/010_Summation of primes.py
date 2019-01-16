# -*- coding: utf-8 -*-
import math

def isPrime(n):
	r = True
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			r = False
			break
	return r

s = 0
for i in range(2, 2000000):
	if isPrime(i):
		s = s + i
print(s)