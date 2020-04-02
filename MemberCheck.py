def whosDishonest(club1, club2, club3):
	club1and2=set(club1).intersection(club2)
	club1and3=set(club1).intersection(club3)
	club2and3=set(club2).intersection(club3)
	union=club1and2.union(club1and3)
	union=union.union(club2and3)
	lies=list(union)

	return lies

def main():

	#Example one
	"""
	club1=["JOHN","JOHN", "FRED", "PEG"]
	club2=["PEG", "GEORGE"]
	club3=["GEORGE", "DAVID"]
	"""
	
	#Example two
	"""
	club1=["DOUG","DOUG", "DOUG", "DOUG"]
	club2=["BOBBY", "BOBBY"]
	club3=["JAMES"]
	"""
	#Example three
	"""
	club1=["BOBBY"]
	club2=["BOB", "BOBBY"]
	club3=["BOB"]
	"""
	#Example four

	"""
	club1=["BOBBY","HUGH", "LIZ", "GEORGE"]
	club2=["ELIZABETH","WILL"]
	club3=["BOB","BOBBY","BOBBY","PAM","LIZ","BOBBY","BOBBY","WILL"]
	"""

	#Example five
	"""
	club1=["JAMES","HUGH","HUGH","GEORGE","ELIZABETH","ELIZABETH","HUGH","DAVID","ROBERT","DAVID","BOB","BOBBY","PAM","JAMES","JAMES"]
	club2=["BOBBY","ROBERT","GEORGE","JAMES","PEG","JAMES","DAVID","JOHN","LIZ","SANDRA","GEORGE","JOHN","GEORGE","ELIZABETH","LIZ","JAMES"]
	club3=["ROBERT","ROBERT","ROBERT","SANDRA","PAM","BOB","LIZ","GEORGE"]

	"""
	#Example six
	"""
	club1=["LIZ","WILL","JAMES"]
	club2=["JOHN","ROBERT","GEORGE","LIZ","PEG","HUGH","BOB","BOBBY","ROBERT","ELIZABETH","DAVID"]
	club3=["PAM","DAVID","SANDRA","GEORGE","JOHN","ROBERT","SANDRA","GEORGE"]
	"""
	#Example seven

	club1=["PEG","ROBERT","PAM","JOHN","DAVID","JOHN","ROBERT","GEORGE","HUGH","WILL","JAMES","JAMES","BOBBY","BOBBY","SANDRA"]
	club2=["SANDRA","BOB","PAM","JAMES","WILL","DAVID","BOBBY","GEORGE","WILL","LIZ","BOBBY","ROBERT","WILL","BOB","BOBBY","ELIZABETH","HUGH"]
	club3=["WILL","PEG","ELIZABETH","DAVID","HUGH","BOBBY","JOHN","SANDRA","ELIZABETH","ELIZABETH","SANDRA","GEORGE","PAM","ELIZABETH","BOBBY","DAVID","PAM"]
	

	liers=whosDishonest(club1, club2, club3)
	print(sorted(liers))

if __name__ == '__main__':
	main()

