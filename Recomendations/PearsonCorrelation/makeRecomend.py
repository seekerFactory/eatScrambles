import regex, argparse
from recomends import PModel as PM


def main():
	print("################")


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Check my recomendations', add_help=True)
	parser.add_argument('-v', '--verbose',dest='verbose', action='store_true', help='verbose mode processing shown')
	parser.add_argument('-t', '--test',dest='testcase', action='store', choices={'movie', 'food'}, default='movie',help='testcase name')
	parser.add_argument('-q', '--quit', dest='quit', action='store_true', help='quit now')


	args=parser.parse_args()

	if args.verbose:
		print(args.verbose)
	else:   print(args.testcase)

	main()
