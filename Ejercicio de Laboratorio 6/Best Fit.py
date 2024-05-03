# Best Fit

#Asignarle un espacio de memoria a los bloques
def bestFit(blockSize, m, processSize, n): 
	
	# asigna un bloque a un proceso
	allocation = [-1] * n 
	
	# busca bloques candidatos
	for i in range(n): 
		
		# encuentra el mejor bloque
		bestIdx = -1
		for j in range(m): 
			if blockSize[j] >= processSize[i]: 
				if bestIdx == -1: 
					bestIdx = j 
				elif blockSize[bestIdx] > blockSize[j]: 
					bestIdx = j 

		# Asigna a ese bloque ideal y resta la memoria usada al bloque
		if bestIdx != -1: 
			
			allocation[i] = bestIdx 

			blockSize[bestIdx] -= processSize[i] 

	print("Process No. Process Size	 Block no.") 
	for i in range(n): 
		print(i + 1, "		 ", processSize[i], 
								end = "		 ") 
		if allocation[i] != -1: 
			print(allocation[i] + 1) 
		else: 
			print("Not Allocated") 

if __name__ == '__main__': 
	blockSize = [100, 500, 200, 300, 600] 
	processSize = [212, 417, 112, 426] 
	m = len(blockSize) 
	n = len(processSize) 

	bestFit(blockSize, m, processSize, n) 
	
