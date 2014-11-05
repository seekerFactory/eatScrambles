#! /usr/bin/env python3

from math import sqrt


# dictionary of movie critics and their ratings of a small
# set of movies

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
 'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,'You, Me and Dupree': 3.5},
 'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
 'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
 'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
 'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def transformPrefs(prefs):
	"""
	transform dict for items from persons
	returns list of tuples
	"""
	result={}

	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item, {})
			# flip item and person
			result[item][person]=prefs[person][item]


	return result




def sim_pearson(prefs, p1, p2):
	"""
	Returns the Pearson correlation coefficient for p1 and p2
	Also handles grade inflation, similar elements
	returns value bw(-1 and +1), +1 means p1 and p2 have save score for every elements.
	"""
	# get list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1

	
	# number of elements
	n=len(si)

	# if no ratings in common return 0
	if n==0: return 0
	# add up all preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])
	# sum up all squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
	# sum up all products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

	# pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
	if den==0: return 0

	r=num/den

	return r


def topMatches(prefs, item, n=5, similarity=sim_pearson):
	"""
	Returns best matches for item from prefs dict.
	Number of top n results and similarity function are optional params.
	"""
	scores=[(similarity(prefs, item, other), other)
			for other in prefs if other!=item]

	scores.sort()
	scores.reverse()
	return scores[0:n]

