#if/elif
x=12
y=4
if x>10:
	print 'a'
if y<5:
	print 'b'
else:
	print c

x = 1500
big = x>1000
if big:
	print 'big'

#for
nums = {"first":1, "second":2}
sum = 0
for num in nums:
	print num

for x in range(5,10,2):
	print x

#while loop
small = True
sum = 0
while small:
	sum = sum + 1
	if sum > 5:
		small = False
