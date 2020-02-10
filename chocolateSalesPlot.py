import matplotlib.pyplot as plt

def plotChocolate(barNumbers, Averages):
	plt.plot(barNumbers, Averages)
	plt.show()

def calculateBars(dollars):
	tickets=dollars
	bars=dollars
	#print(bars)
	#print(tickets)
	while(tickets>=10):

		bars+=1
		tickets-=9
		#print(bars)
		#print(tickets)
	return round(dollars/bars, 3)
	# may want to ensure float.

def main():
	barNum=[]
	barStats=[]
	for number in range(20,101):
		barNum.append(number)
		barStats.append(calculateBars(number))
	plotChocolate(barNum,barStats)


if __name__ == '__main__':
	main()