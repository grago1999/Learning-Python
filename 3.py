def myFunction(num, str):
	if num > 4:
		print(num)
	else:
		print(str)
		mySecondFunction()


def mySecondFunction():
	print(2)


myFunction(3, "hello")
myFunction(6, "hello2")

input = raw_input("What is your name?")

print("Your name is " + input)

string = "A o haha o string of words"

stringlist = string.split()

print("our stringlist: ", stringlist)

stringlist2 = string.split("o")

print("our stringlist2: ", stringlist2)

