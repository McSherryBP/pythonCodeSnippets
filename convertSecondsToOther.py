sec=int(input())

seconds=sec
minutes=0
hours=0
days=0
years=0

if sec>=60:
	seconds=sec%60

minutes=sec/60

if minutes>=60:
	hours=minutes/60
	minutes=minutes%60

if hours>=24:
	days=hours/24
	hours=hours%24

if days>=365:
	years=days/365
	days=days%365

print("Years: %d" % years)
print("Days: %d" % days)
print("Hours: %d" % hours)
print("Minutes: %d" % minutes)
print("Seconds: %d" % seconds)
