# -*- coding: utf-8 -*-

for i in range(1, 1000):
	for j in range(1, 1000):
		if i * i + j * j == (1000-i-j) ** 2:
			print(i * j * (1000-i-j))