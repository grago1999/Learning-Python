#November 17, 2016 -- Practice Problems

"""
Write a function, ishashad that determines whether a number is a Harshad
number (for number base 10).
A Harshad number is an integer that is divisible by the sum of its digits”
(Wikipedia)
Example: 81 → 8 + 1 = 9 → 81/9 = 9 → Harshad!
>>> ishashad(81)
True
"""

def isharshad(x):
	xstring = str(x)
	sum = 0
	for digit in xstring: 
		sum += int(digit)
	xdivisible = x%sum == 0

	return xdivisible

#http://codingbat.com/prob/p182414

#http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

"""
11. Write a Python function to check whether a number is perfect or not. Go to the editor
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128. 
Source: http://www.w3resource.com/python-exercises/python-functions-exercises.php
"""