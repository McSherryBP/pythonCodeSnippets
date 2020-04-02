#Python 3.7
#Brendan McSherry

#The time and, goal, and inital states are hardcoded.
#t=time(step), at(1,1) is the initial state of the bot, goal is (3,3).


def main():

	"""
	dict={
	"node11":True,
	"node12":False,
	"node13":False,
	"node14":False,
	"node21":False,
	"node22":False,
	"node23":False,
	"node24":False,
	"node31":False,
	"node32":False,
	"node33":False,
	"node34":False,
	"node41":False,
	"node42":False,
	"node43":False,
	"node44":False,
	}
	
	while(dict["node33"]==False):
		if(dict["node11"] or dict["node12"] or dict["node13"] or dict["node14"] or dict["node21"] or dict["node22"] or dict["node23"] or dict["node24"]):
			goRightGround() 
	"""
	
	t=0

	at=[1,1]
	goal=(3,3)
	
	print(at)
	print(t)

	while(at[0]!=goal[0] or at[1]!=goal[1]):
		t+=1
		if(at[0]<goal[0]):
			at=goRight(at)
		elif(at[0]>goal[0]):
			at=goLeft(at)
		elif(at[1]<goal[1]):
			at=goUp(at)
		else:
			at=goDown(at)

		print(at)
		print(t)


def goRight(currentAt):
	print("Go Right")
	currentAt[0]+=1
	return currentAt

def goLeft(currentAt):
	print("Go Left")
	currentAt[0]-=1
	return currentAt

def goUp(currentAt):
	print("Go Up")
	currentAt[1]+=1
	return currentAt

def goDown(currentAt):
	print("Go Down")
	currentAt[1]-=1
	return currentAt

if __name__=="__main__":
	main()

