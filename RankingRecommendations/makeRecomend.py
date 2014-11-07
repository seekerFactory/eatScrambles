#! /usr/bin/env python3

import argparse, random

from data import *
from recomends import RModel as RM
from tests import tested, testTopNMatches

#tested(rmnd, testcase='movie', verbose=False):

def main():
	print("################")

	# will keep only one object always
	# other place where obj is created is test main() only tests.py directly ran
	rmnd = RM()
	# data set

	if args.testcase:
		testcase=args.testcase
		if testcase == 'movie':
			critics=movie_critics
		if testcase == 'food':
			critics=food_critics

	rmnd=RM()
	if(args.critic):
		critic_name=args.critic
	else:
		# Choose critic at random
		ci=[]
		ci=rmnd.getCritics(critics)

		critic_name=ci[random.randrange(len(ci)-1)]
	
	tested(rmnd, critics, testcase, critic_name)




if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Recomendations and Ranking', add_help=True)
	parser.add_argument('-v', '--verbose',dest='verbose', action='store_true', help='verbose mode processing shown')
	parser.add_argument('-t', '--test',dest='testcase', action='store', choices={'movie', 'food'}, default='movie',help='testcase name')
	parser.add_argument('-c', '--critic',dest='critic', action='store', help='critic name')
	parser.add_argument('-q', '--quit', dest='quit', action='store_true', help='quit now')


	args=parser.parse_args()

	if args.verbose:
		print(args.verbose)
	else:   print(args.testcase)

	main()
