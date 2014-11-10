#! /usr/bin/env python3

from math import sqrt


class RModel:

	def getCritics(self, critics):
		"""
		Returns list of all critics from dataset
		"""
		ci=[]
		for critic in critics: ci.append(critic)
		return ci

	def getCriticPreferences(self, critics, critic):
		"""
		Return all recommendations from a critic, with score
		"""
		si={}
		si=critics[critic]
		return si


	def sim_pearson(self, prefs, p1, p2):
		"""
		Returns the Pearson correlation coefficient for p1 and p2
		Also handles grade inflation, similar elements
		returns value bw(-1 and +1), +1 means p1 and p2 have same score for every elements.
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
	



	# Gets recommendations for a person by using a weighted average
	# of every other user's rankings
	def getRecommendations(self, prefs, person):
		totals={}
		simSums={}
		
		for other in prefs:
			# don't compare me to myself
			if other==person: continue
			sim=self.sim_pearson(prefs,person,other)
			
			# ignore scores of zero or lower
			if sim<=0: continue
			for item in prefs[other]:
				# only score movies I haven't seen yet
				if item not in prefs[person] or prefs[person][item]==0:
					# Similarity * Score
					totals.setdefault(item,0)
					totals[item]+=prefs[other][item]*sim
					# Sum of similarities
					simSums.setdefault(item,0)
					simSums[item]+=sim

		# Create the normalized list
		rankings=[(total/simSums[item],item) for item,total in totals.items()]
		# Return the sorted list
		rankings.sort( )
		rankings.reverse( )
		return rankings



	def topMatches(self, prefs, item, n=5):
		"""
		Returns best matches for item from prefs dict.
		Number of top n results are optional params.
		-ve score for an item means those who liked item specified, tend to dislike other item specified in -ve score
		"""
		#scores=[(similarity(prefs, item, other), other)
		scores=[(self.sim_pearson(prefs, item, other), other)
				for other in prefs if other!=item]
	
		scores.sort()
		scores.reverse()
		return scores[0:n]
	


	def calculateSimilarItems(self, prefs,n=10):
		# Create a dictionary of items showing which other items they
		# are most similar to.
		result={}
	
		# Invert the preference matrix to be item-centric
		itemPrefs=self.transformPrefs(prefs)
	
		c=0
		for item in itemPrefs:
			# Status updates for large datasets
			c+=1
			if c%100==0: print("%d / %d" % (c,len(itemPrefs)))
			# Find the most similar items to this one
			#scores=self.topMatches(itemPrefs,item,n=n,self.sim_distance)
			scores=self.topMatches(itemPrefs,item,n=n)
			result[item]=scores
	
		return result
	
	
	
	
	def transformPrefs(self, prefs):
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
	


	def getRecommendedItems(self, prefs,itemMatch,user):
		userRatings=prefs[user]
		scores={}
		totalSim={}

		# Loop over items rated by this user
		for (item,rating) in userRatings.items():
			# Loop over items similar to this one
			for (similarity,item2) in itemMatch[item]:
				# Ignore if this user has already rated this item
				if item2 in userRatings: continue
				# Weighted sum of rating times similarity
				scores.setdefault(item2,0)
				scores[item2]+=similarity*rating

				# Sum of all the similarities
				totalSim.setdefault(item2,0)
				totalSim[item2]+=similarity

		# Divide each total score by total weighting to get an average
		rankings=[(score/totalSim[item],item) for item,score in scores.items()]

		# Return the rankings from highest to lowest
		rankings.sort( )
		rankings.reverse( )
		return rankings


