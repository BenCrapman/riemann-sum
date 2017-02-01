#Developed by Ben Chapman
import math

#this function takes a string representing a function of y with respect to x
#the function returns the y value at a given x
def execute_function(function_string, x):
	y = eval(function_string)
	return y

#give the user some information
print 'You must enter a function y in terms of x.'
print 'The function must be formatted in a way that python will recognize.'
print 'for a list of possible functions, read the "functions.txt" file'
print '\n'

#get a string representing our function, as well as a slice width
function = raw_input('function: y = ')

#newline
print '\n'

#print f(0) through f(10)
for i in range(10):
	print 'f(' + str(i) + ') = ' + str(execute_function(function, i))
