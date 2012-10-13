#!/usr/bin/env python

#!/usr/bin/env python

#	Project 3 - Netflix
#	Brett Canino
#	Instructor - Glenn Downing
#	Cs 373
#	Netflix.py

# -------------
# netflix_solve
# -------------
def netflix_start (r, w) :
	"""
	calls methods to create average rating and creates user
		and movie caches from files then calls eval
	r is a reader
	w is a writer
	"""

	user_cache = {}
	netflix_user_cache(user_cache)
	
	movie_cache = {}
	netflix_movie_cache(movie_cache)
	
	avg_rating = netflix_average_rating(user_cache)
	
	assert type(avg_rating) is float
	assert type(user_cache) is dict
	assert type(movie_cache) is dict
	assert user_cache			# asserts that user_cache is not empty
	assert movie_cache			# asserts that movie_cache is not empty
	
	netflix_eval(r, w, avg_rating, user_cache, movie_cache)

	
# ------------
# netflix_eval
# ------------
def netflix_eval(r, w, avg_rating, user_cache, movie_cache) :
	"""
	reads input file and makes a predicted rating of movies
		and then writes them to a file
	user_cache is a cache containing user_cache average rating
	movie_cache is a cache containing average ratings for each movie
	r is a reader
	w is a writer
	avg_rating is the overall average rating
	"""
	
	assert type(avg_rating) is float
	assert avg_rating > 0
	assert movie_cache		# asserts that movie_cache is not empty
	assert user_cache			# asserts that user_cache is not empty
	
	movie_off = 0.0
	user_off = 0.0
	prediction = 0.0
	for line in r:
	
		s = line.split(":")
		if len(s) == 2 :
		
			movie_id = s[0]
			movie_rating = movie_cache[movie_id]
			assert type(movie_rating) is float
			movie_off = netflix_movie_offset(avg_rating, movie_rating)
			w.write(line)
			
		else :
		
			assert len(s) == 1
	
			user_id = s[0].strip()
			user_rating = user_cache[int(user_id)]
			
			assert type(user_rating) is float
			
			movie_off = netflix_movie_offset(avg_rating, movie_rating)
			user_off = netflix_user_offset(avg_rating, user_rating)
			prediction = avg_rating + movie_off + user_off
			
			assert type(prediction) is float
			
			w.write(user_id + "," +  str(prediction) + "\n")
	
	assert user_off != 0
	assert movie_off != 0

# --------------------
# netflix_movie_offset
# --------------------
def netflix_movie_offset(avg_rating, movie_rating) :
	"""
	returns offset from overall average rating and this movies average rating
	avg_rating is the overall average rating
	movie_rating is the average rating for this movie
	"""
	
	assert avg_rating > 0
	assert movie_rating > 0
	
	return movie_rating - avg_rating

	
# -------------------
# netflix_user_offset
# -------------------
def netflix_user_offset(avg_rating, user_rating) :
	"""
	returns offset from average user rating and this movies average rating
	user_rating is the average rating for this user
	movie_rating is the average rating for this movie
	"""
	
	assert user_rating > 0
	assert avg_rating > 0
	
	return user_rating - avg_rating


# ------------------
# netflix_user_cache
# ------------------
def netflix_user_cache(user_cache) :
	"""
	Creates a cache containing users average ratings
	user_cache is a dict containing nothing at first and all the avg user data at the end 
	"""
	
	assert user_cache == {}		# asserts that user_cache is empty at start
	
	file_name = "UserRatingsCache.txt"
	uFile = open(file_name, 'r')
	for line in uFile :
		s = line.split("-")
		
		if len(s) == 2 :
			user_cache[int(s[0])] = float(s[1])
			assert type(user_cache[int(s[0])]) is float
	
	assert user_cache			# asserts that user_cache is not empty


# -------------------
# netflix_movie_cache
# -------------------
def netflix_movie_cache(movie_cache) :
	"""
	Creates a cache containing movies average ratings
	movie_cache is a dictionary containing nothing at first and all 
		the movie data at the end 
	"""
	
	assert movie_cache == {}	# asserts that movie_cache is empty at start
	
	file_name = "MovieRatingsCache.txt"
	mFile = open(file_name, 'r')
	
	for line in mFile :
		s = line.split(":")
		movie_cache[s[0]] = float(s[1])
		assert type(movie_cache[s[0]]) is float
	
	assert movie_cache		# asserts that movie_cache is not empty

# ----------------------
# netflix_average_rating
# ----------------------
def netflix_average_rating(user_cache) :
	"""
	Returns the average overall rating made by any user
	user_cache is a dictionary that contains the average of all user_cache ratings
	"""
	
	assert user_cache			# asserts that user_cache is not empty
	
	total = 0.0
	count = 0.0
	for a, b in user_cache.items() :
		total += b
		count += 1
	
	avg = total/count
	
	assert type(avg) is float
	assert avg > 0
	
	return avg
	
