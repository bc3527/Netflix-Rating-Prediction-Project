#!/usr/bin/env python

#	Project 3 - Netflix
#	Brett Canino
#	Instructor - Glenn Downing
#	Cs 373
#	TestNetflix.py

"""
To test the program:
    % python TestNetflix.py >& TestNetflix.py.out
    % chmod ugo+x TestNetflix.py
    % TestNetflix.py >& TestNetflix.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Netflix import netflix_start, netflix_eval, netflix_movie_offset, netflix_user_offset, netflix_user_cache, netflix_movie_cache, netflix_average_rating

# -----------
# TestNetflix
# -----------

class TestNetflix (unittest.TestCase) :

    # -----
    # start
    # -----

			# no reason or easy way to test start, it just 
			# calls other methods that will be tested below
			# and passes on a reader and a writer and returns
			# no value
	
    # ----
    # eval
    # ----

	def test_eval_1(self):
		r = ["1:\n","20"]
		avg = 3.0
		user_cache = {}
		user_cache[20] = 5.0
		movie_cache = {}
		movie_cache["1"] = 4.0
		w = StringIO.StringIO()
		netflix_eval(r, w, avg, user_cache, movie_cache)
		self.assert_(w.getvalue() == "1:\n20,6.0\n")

	def test_eval_2(self):
		r = ["1:\n","20\n","2:\n","30"]
		avg = 1.0
		user_cache = {}
		user_cache[20] = 3.0
		user_cache[30] = 5.0
		movie_cache = {}
		movie_cache["1"] = 1.0
		movie_cache["2"] = 2.0
		w = StringIO.StringIO()
		netflix_eval(r, w, avg, user_cache, movie_cache)
		self.assert_(w.getvalue() == "1:\n20,3.0\n2:\n30,6.0\n")

	def test_eval_3(self):
		r = ["15000:\n","342\n","23233:\n","1\n","17770:\n","2500000"]
		avg = 0.5
		user_cache = {}
		user_cache[342] = 4.323
		user_cache[1] = 2.332
		user_cache[2500000] = 3.111		
		movie_cache = {}
		movie_cache["15000"] = 4.9
		movie_cache["23233"] = 3.4433
		movie_cache["17770"] = 1.1112
		w = StringIO.StringIO()
		netflix_eval(r, w, avg, user_cache, movie_cache)
		answer = avg + (5.0 - avg) + (4.0 - avg)
		self.assert_(w.getvalue() == "15000:\n342,8.723\n23233:\n1,5.2753\n17770:\n2500000,3.7222\n")
		
	# ------------
	# movie_offset
	# ------------
	
	def test_movie_offset_1(self):
		avg = 3.0
		movie = 4.0
		x = 0.0
		x = netflix_movie_offset(avg, movie)
		actual = 1.0
		self.assert_(type(x) is float)
		self.assert_(type(actual) is float)
		self.assert_(x == actual)
		
	def test_movie_offset_2(self):
		avg = 2.73
		movie = 4.73
		x = 0.0
		x = netflix_movie_offset(avg, movie)
		actual = movie - avg
		self.assert_(type(x) is float)
		self.assert_(type(actual) is float)
		self.assert_(x == actual)
		
	def test_movie_offset_3(self):
		avg = 1.34
		movie = 3.45
		x = 0.0
		x = netflix_movie_offset(avg, movie)
		actual = movie - avg
		self.assert_(type(x) is float)
		self.assert_(type(actual) is float)
		self.assert_(x == actual)

	# -----------
	# user_offset
	# -----------
	
	def test_user_offset_1(self):
		avg = 3.3434345
		user = 4.4355
		x = 0.0
		x = netflix_user_offset(avg, user)
		actual = user - avg
		self.assert_(type(x) is float)
		self.assert_(type(actual) is float)
		self.assert_(x == actual)
		
	def test_user_offset_2(self):
		avg = 3.6784
		user = 2.342
		x = 0.0
		x = netflix_user_offset(avg, user)
		actual = user - avg
		self.assert_(type(x) is float)
		self.assert_(type(actual) is float)
		self.assert_(x == actual)
		
	def test_user_offset_3(self):
		avg = 1.234
		user = 4.0
		x = 0.0
		x = netflix_user_offset(avg, user)
		actual = user - avg
		self.assert_(type(x) is float)
		self.assert_(type(actual) is float)
		self.assert_(x == actual)
	

	# ----------
	# user_cache
	# ----------

	def test_user_cache_1 (self) :
		uCache = {}
		netflix_user_cache(uCache)
		
		self.assert_(uCache)		# False is uCache is empty
		
	def test_user_cache_2 (self) :
		uCache = {}
		netflix_user_cache(uCache)
		for a,b in uCache.items() :
			self.assert_(type(a) is int)
		
	def test_user_cache_3 (self) :
		uCache = {}
		netflix_user_cache(uCache)
		for a,b in uCache.items() :
			self.assert_(type(b) is float)
		

	# -----------
	# movie_cache
	# -----------
	
	def test_movie_cache_1 (self) :
		mCache = {}
		netflix_movie_cache(mCache)
		
		self.assert_(mCache)		# False is uCache is empty
		
	def test_movie_cache_2 (self) :
		mCache = {}
		netflix_movie_cache(mCache)
		for a,b in mCache.items() :
			self.assert_(type(a) is str)
		
	def test_movie_cache_3 (self) :
		mCache = {}
		netflix_movie_cache(mCache)
		for a,b in mCache.items() :
			self.assert_(type(b) is float)


	# --------------
	# average_rating
	# --------------

	def test_average_1 (self) :
		cache = {1: 2.334, 2: 3.324, 3: 1.443}
		avg = netflix_average_rating(cache)
		actual = (2.334 + 3.324 + 1.443)/3
		
		self.assert_(type(avg) is float)
		self.assert_(actual == avg)
		
	def test_average_2 (self) :
		cache = {1: 2.3, 2: 3.2, 3: 1.5, 4: 4.1, 5: 3.7, 6: 1.1}
		avg = netflix_average_rating(cache)
		actual = (2.3 + 3.2 + 1.5 + 4.1 + 3.7 + 1.1)/6
		
		self.assert_(type(avg) is float)
		self.assert_(actual == avg)
		
	def test_average_3 (self) :
		cache = {1: 0.1, 2: 0.1, 3: 0.1}
		avg = netflix_average_rating(cache)
		actual = (0.1 + 0.1 + 0.1)/3
		
		self.assert_(type(avg) is float)
		self.assert_(actual == avg)
		
# ----
# main
# ----

print "Testnetflix.py"
unittest.main()
print "Done."