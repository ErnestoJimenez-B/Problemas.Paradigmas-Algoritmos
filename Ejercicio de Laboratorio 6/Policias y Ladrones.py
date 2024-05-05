# Programa policias y ladrones

def policeThief(arr, n, k):
	i = 0
	l = 0
	r = 0
	res = 0
	thi = []
	pol = []

	while i < n:
		if arr[i] == 'P':
			pol.append(i)
		elif arr[i] == 'T':
			thi.append(i)
		i += 1

	# buscar ladrones
	while l < len(thi) and r < len(pol):

		# en caso de que pueda ser atrapado
		if (abs(thi[l] - pol[r]) <= k):
			res += 1
			l += 1
			r += 1

		
		elif thi[l] < pol[r]:
			l += 1
		else:
			r += 1

	return res


if __name__ == '__main__':
	arr1 = ['P', 'T', 'T', 'P', 'T']
	k = 2
	n = len(arr1)
	print(("Maximum thieves caught: {}".
		format(policeThief(arr1, n, k))))

	arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
	k = 2
	n = len(arr2)
	print(("Maximum thieves caught: {}".
		format(policeThief(arr2, n, k))))

	arr3 = ['P', 'T', 'P', 'T', 'T', 'P']
	k = 3
	n = len(arr3)
	print(("Maximum thieves caught: {}".
		format(policeThief(arr3, n, k))))
