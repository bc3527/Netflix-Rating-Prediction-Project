### Cache maker
### RMSE

# Imports #

import sys

# ------
# Cache
# ------

def cache_start_users(w) :
	cache = {}
	movies = [0]
	
	file_name = "movie_titles.txt"
	read_file = open(file_name, 'r')
	
	for line in read_file :
		s = line.split(',')
		movies.append(s[1])
	
	for m_id in range (1, 17771) :
		file_name = "/u/downing/cs/netflix/training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		cache = user_ratings_cache(read_file, w, cache, movies)
		
	for a,b in cache.items() :
			w.write(a + ":\n")
			for c,d in b.items() :
				avg = d[0]/d[1]
				w.write(c + "--" + str(avg) + "\n")
		
	
		
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
		
def user_ratings_cache(r, w, cache, movies) :
	s = "a"
	mov = 0
	
	for s in r:
		x = s.split(",")
		
		if len(x) == 1 :
			d = s.split(":")
			mov = int(d[0])
			year = movies[mov]
		
		else :
			user_id = x[0]
			if user_id not in cache :
				cache[user_id] = {year: [0.0 + int(x[1]), 1.0]}
		
			else :
				user_id_temp = cache[user_id]
				count = 0
				if year in user_id_temp :
					temp = user_id_temp[year]
					temp[1] += 1
					temp[0] = temp[0] + int(x[1])
					user_id_temp[year] = temp
					
				else :
					user_id_temp[year] = [0.0 + int(x[1]), 1.0]
	return cache

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



