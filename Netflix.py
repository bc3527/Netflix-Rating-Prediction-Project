#!/usr/bin/env python

#!/usr/bin/env python

#	Project 3 - Netflix
#	Brett Canino
#	Instructor - Glenn Downing
#	Cs 373

# -------------
# netflix_solve
# -------------
def netflix_solve (r, w) :
	"""
	calls methods to create average rating and creates user
		and movie caches from files then calls eval
	r is a reader
	w is a writer
	"""

	user_cache = {}
	avg_rating = netflix_user_cache(user_cache)
	
	movie_cache = {}
	netflix_movie_cache(movie_cache)
	
	assert type(avg_rating) is float
	assert type(user_cache) is dict
	assert type(movie_cache) is dict
	assert user_cache		# asserts that user_cache is not empty
	assert movie_cache		# asserts that movie_cache is not empty
	
	netflix_eval(user_cache, movie_cache, r, w, avg_rating)

	
# -------------
# netflix_eval
# -------------
def netflix_eval(user_cache, movie_cache, r, w, avg_rating) :
	"""
	reads input file and makes a predicted rating of movies
		and then writes them to a file
	user_cache is a cache containing users average rating for each year
	movie_cache is a cache containing average ratings for each movie
	r is a reader
	w is a writer
	avg_rating is the overall average rating
	"""
	
	assert type(avg_rating) is float
	assert avg_rating > 0
	assert user_cache		# asserts that user_cache is not empty
	assert movie_cache		# asserts that movie_cache is not empty
	
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
			user_rating = user_cache[user_id]
			assert type(user_rating) is float
			user_off = netflix_user_offset(movie_rating, user_rating)
			year_off = netflix_year_offset(year_rating, user_rating)
			prediction = avg_rating + movie_off + user_off + year_off
			w.write(user_id + "," +  str(prediction) + "\n")
	
	assert prediction > 0
	assert user_off > 0
	assert movie_off > 0
	assert year_off > 0

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

	
# --------------------
# netflix_user_offset
# --------------------
def netflix_user_offset(movie_rating, user_rating) :
	"""
	returns offset from average user rating and this movies average rating
	user_rating is the average rating for this user
	movie_rating is the average rating for this movie
	"""
	
	assert user_rating > 0
	assert movie_rating > 0
	
	return user_rating - movie_rating

	
# --------------------
# netflix_year_offset
# --------------------	
def netflix_year_offset(year_rating, user_rating) :
	"""
	returns offset from average user rating and the users average rating 
		for this movies year
	user_rating is the average rating for this user
	year_rating is the average rating for this user for this year
	"""
	
	assert user_rating > 0
	assert year_rating > 0
	
	return year_rating - user_rating

	
# --------------------
# netflix_user_cache
# --------------------
def netflix_user_cache(user_cache) :
	"""
	Creates a cache containing user rating data including the year
	user_cache is a dictionary containing nothing at first and all 
		the user data at the end 
	"""
	
	assert user_cache == {}		# asserts that user_cache is empty at start
	
	file_name = "UserRatingsCache.txt"
	uFile = open(file_name, 'r')
	count = 0
	sum = 0.0
	for line in uFile :
		s = line.split(":")
		if len(s) == 2 :
			user_id = s[0]
			user_cache[user_id] = 0
		else :
			s = line.split("--")
			user_dict = user_cache[user_id]
			if user_dict == 0 :
				user_dict = {s[0]: float(s[1])}
				user_cache[user_id] = user_dict
			else :
				user_dict[s[0]] = float(s[1])
				user_cache[user_id] = user_dict

			count += 1
			sum += float(s[1])
	
	assert sum > 0
	assert count > 0
	assert user_cache		# asserts that user_cache is not empty
	
	return sum/count


# --------------------
# netflix_movie_cache
# --------------------
def netflix_movie_cache(movie_cache) :
	"""
	Creates a cache containing movies average ratings
	movie_cache is a dictionary containing nothing at first and all 
		the movie data at the end 
	"""
	
	assert movie_cache == {}	# asserts that movie_cache is empty at start
	
	file_name = "MovieRatingsCache.txt"
	uFile = open(file_name, 'r')
	for line in uFile :
		s = line.split(":")
		movie_cache[s[0]] = float(s[1])
	
	assert movie_cache		# asserts that movie_cache is not empty
	
	