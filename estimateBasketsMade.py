import random;


def g(bins):
	a= [0]*bins
	total=1
	for i in range(1, len(a)):
		basket=random.randint(0,len(a)-1)
		if a[basket]==1:
			break
		else:
			a[basket]=1
		total+=1
	return total

def main():

	basketCount=1000
	duplicateRates=[0]*basketCount
	for trial in range(0, len(duplicateRates)):
		duplicateRates[trial]=g(basketCount)
	print("Expected Number of tosses for "+str(basketCount)+ " baskets: "+ str(sum(duplicateRates)/len(duplicateRates)))


if __name__ == '__main__':
	main()