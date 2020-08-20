Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input())
10
>>> if n%4 == 0:
	print('Fizz')
elif n%7 == 0:
	print('Buzz')
elif n%4 == 0 and n%7 == 0:
	print('FizzBuzz')

	
>>> n = 4
>>> n = int(input())
4
>>> print n
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(n)?
>>> print(n)
4
>>> 