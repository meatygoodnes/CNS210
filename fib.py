import argparse
# Do the fibonacci calculations 
def fib(n):
	a, b = 0, 1 
	for i in range(n):
		a, b = b, a+b
	return a

# set up argparse 
def Main():
	parser = argparse.ArgumentParser()
# use mutually exclusive groups (either/or) to make options
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", help="Gives a detailed answer", action="store_true")
	group.add_argument("-q", "--quiet", help="Gives just the answer", action="store_true")
	parser.add_argument("num", help=" The number of fironacci iterations you wish to calculate", type=int)
	parser.add_argument("-o", "--output", help="Use this option to write to a file called fibrnacci.txt", action="store_true")
# parse the argeuemtns to the parser
	args = parser.parse_args()

# print the results
	result = fib(args.num)
	if args.verbose:
		print("The "+str(args.num)+"th fib number is "+str(result))
	elif args.quiet:
		print(result)
	else:
		print("Fib("+str(args.num)+") = "+str(result))

# write the results to a file 
	if args.output:
		f = open("fibrnacci.txt", "a")
		f.write(str(result)+ '\n')
		f.close()

# this runs the parser
if __name__ == '__main__':
	Main()
