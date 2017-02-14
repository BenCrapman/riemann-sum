#Developed by Ben Chapman
import math

#this function takes a string representing a function of y with respect to x
#the function returns the y value at a given x
def execute_function(function_string, x):
	y = eval(function_string)
	return y

#this function returns a left-handed riemann sum
#given a function, slice width, beginning x, and end x
def riemann(string_function, dx, a, b):
	area = 0.0
	x = 0.0
	n = int((b - a) / dx)
	for i in range(n):
		x = a + dx * i
		x = execute_function(string_function, x) * dx
		area += x
	return area

#define variables
slice_width = 0.0;
beginning = 0;
end = 0;
answer = 0;

#give the user some information
print 'You must enter a function y in terms of x.'
print 'The function must be formatted in a way that python will recognize.'
print 'for a list of possible functions, read the "functions.txt" file.'
print '\n'

#get a string representing our function
function = raw_input('function: y = ')

#newline
print '\n'

#give the user more information
print 'You must now enter the width of each slice.'
print 'You\'ll probably want something around 0.1 or 0.01.'
print 'The smaller the slice width, the more precise the answer.'
print '\n'

#get slice width from the user
slice_width = raw_input('slice width: dx = ')

#newline
print '\n'

#more info
print 'Now, enter the interval over which you want to integrate.'
print '\n'

#get interval
beginning = raw_input('Beginning: x = ')
end = raw_input('End: x = ')

#newline
print '\n'

#convert strings that should be floats to floats
slice_width = float(slice_width)
beginning = float(beginning)
end = float(end)

#get the riemann sum
answer = riemann(function, slice_width, beginning, end)

#print the riemann sum
print 'The riemann sum is: ' + str(answer)

print '\n'
