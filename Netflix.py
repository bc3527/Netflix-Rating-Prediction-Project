#!/usr/bin/env python

#!/usr/bin/env python

#	Project 3 - Netflix
#	Brett Canino
#	Instructor - Glenn Downing
#	Cs 373


def netflix_solve (r, w) :

	user_cache = {}
	avg_rating = netflix_user_cache(user_cache)
	assert type(avg_rating) is float
	
	movie_cache = {}
	netflix_movie_cache(movie_cache)
	
	netflix_eval(user_cache, movie_cache, r, w, avg_rating)
	
def netflix_eval(user_cache, movie_cache, r, w, avg_rating) :
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
			user_off = netflix_user_offset(avg_rating, user_rating)
			prediction = avg_rating + movie_off + user_off
			w.write(user_id + "," +  str(prediction) + "\n")
		
	
def netflix_movie_offset(avg_rating, movie_rating) :
	return movie_rating - avg_rating


def netflix_user_offset(avg_rating, user_rating) :
	return user_rating - avg_rating

def netflix_user_cache(user_cache) :
	file_name = "UserRatingsCache.txt"
	uFile = open(file_name, 'r')
	count = 0
	sum = 0.0
	for line in uFile :
		s = line.split("--")
		user_cache[s[0]] = float(s[1])
		count += 1
		sum += float(s[1])
		
	return sum/count
		
def netflix_movie_cache(movie_cache) :
	file_name = "MovieRatingsCache.txt"
	uFile = open(file_name, 'r')
	for line in uFile :
		s = line.split(":")
		movie_cache[s[0]] = float(s[1])
	






# ------------
# collatz_read
# ------------
 
def netflix_read (r, a) :
    """
    opens 
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True
 