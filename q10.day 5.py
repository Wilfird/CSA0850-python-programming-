from random import randint
def randomize (arr, n):	
	for i in range(n-1,0,-1):
		j = randint(0,i+1)		
		arr[i],arr[j] = arr[j],arr[i]
	return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)
print(randomize(arr, n))

