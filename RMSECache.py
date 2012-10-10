### Cache maker
### RMSE

# Imports #

import sys

# ------
# Cache
# ------

def cache_start_users(w) :

	for m_id in range (1, 17771) :
		file_name = "/u/downing/cs/netflix/training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		user_ratings_cache(read_file, w)
		
def cache_start_movies(w) :

	for m_id in range (1, 17771) :
		file_name = "/u/downing/cs/netflix/training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		movie_ratings_cache(read_file, w)


def movie_ratings_cache( r, w ) :
	cache = [0]
	cache[0] = "null"
	index = 0
	avg = 0
	count = 0.0
	s = "a"
	movie_id = ""
	
	while (s != "") :

		s = r.readline()
		x = s.split(",")
		
		if len(x) == 1 :
		
			x = s.split(":")
			if cache[0] == "null" :
				cache[0] = "progress"
				movie_id = x[0]
		
			else :
				avg = avg/count
				if cache[0] == "progress" :
					cache =[[movie_id, avg]]
				else :
					cache.append([movie_id, avg])
				count = 0
				index += 1
				movie_id = x[0]
		
		else :
			count += 1
			avg += int(x[1])
			
	for a in cache :
		w.write(a[0] + ":" + str(a[1]) + "\n")
		
def user_ratings_cache(r, w) :
	cache = [0]*2649430
	s = "a"
	
	while (s != "") :

		s = r.readline()
		x = s.split(",")
		
		if len(x) !=  1 :
			user_id = int(x[0])
			if cache[user_id] == 0 :
				cache[user_id] = [user_id, int(x[1]), 1.0]
		
			else :
				temp = cache[user_id]
				temp[2] += 1
				temp[1] = (temp[1] + int(x[1]))/temp[2]
				cache[user_id] = temp
			
	for a in cache :
		if a != 0 :
			w.write(str(a[0]) + "--" + str(a[1]) + "\n")
	

# ------
# RMSE
# ------



# ------
# run
# ------

# cache_start_users(sys.stdout)
#
# or
#
# cache_start_movies

cache_start_users(sys.stdout)



