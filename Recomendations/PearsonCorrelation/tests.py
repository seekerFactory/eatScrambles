#! /usr/bin/env python3


from data import *
from recomends import PModel as PM



def tested(testcase, verbose=False):
	return


def main():

	critics=movie_critics
	rmnd=PM()


	
	rmnd.topMatches(critics,'Toby',n=3)


if __name__ == '__main__':
	main()
