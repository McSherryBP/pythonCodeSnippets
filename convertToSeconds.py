years=int(input("Enter Number of Years: "))
days=int(input("Enter Number of days: "))
hours=int(input("Enter Number of hours: "))
minutes=int(input("Enter Number of minutes: "))
seconds=int(input("Enter Number of seconds: "))

days+=(365*years)
hours+=(24*days)
minutes+=(60*hours)
seconds+=(60*minutes)

print("Total number of seconds: %d" % seconds)
