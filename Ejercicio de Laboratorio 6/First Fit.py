#first fit

# la función:
def firstFit(blockSize, m, processSize, n): 
	
	# asigna la id del bloque al proceso 
	allocation = [-1] * n 


	# toma cada bloque y lo compara con el proceso para poder asignarlo
	for i in range(n): 
		for j in range(m): 
			if blockSize[j] >= processSize[i]: 
				
				# asignación
				allocation[i] = j 

				# Reducción del bloque
				blockSize[j] -= processSize[i] 

				break

	print(" Process No. Process Size	 Block no.") 
	for i in range(n): 
		print(" ", i + 1, "		 ", processSize[i], 
						"		 ", end = " ") 
		if allocation[i] != -1: 
			print(allocation[i] + 1) 
		else: 
			print("Not Allocated") 

if __name__ == '__main__': 
	blockSize = [100, 500, 200, 300, 600] 
	processSize = [212, 417, 112, 426] 
	m = len(blockSize) 
	n = len(processSize) 

	firstFit(blockSize, m, processSize, n) 
	
