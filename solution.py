# l = [5, 10, 15, 10, 7];
# l = [1, 2, 2, 3, 4]

from __future__ import print_function
def solution(data, n):
	if len(data) < 100:

		l = []
		c = 0
		num = 0
		if n == 1:
			n += 1
		data1 = sorted(data)
		data2 = sorted(data)

		for i in data1:
			for j in data2:
				if j != i:
					c = 0
				if j == i:
					c += 1
					if c >= n:
						num = j
			if num:
				l.append(num)
			num = 0

		for i in data1:
			if i in l:
				data.remove(i)
		print(*data, sep=",")

	else:
		print(" ")

solution([1, 2, 3], 0)
solution([5, 10, 15, 10, 7, 2,], 1)
