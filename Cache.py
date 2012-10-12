### Cache maker
### RMSE

# Imports #

import sys
import time

# ------
# Cache
# ------

def cache_start_users(w) :
	cache = {}
	movies = [0]
	input_users = {}
	input_movies = [0]*17771
	
	file_name = "movie_titles.txt"
	read_file = open(file_name, 'r')
	
	for line in read_file :
		s = line.split(',')
		movies.append(s[1])

	file_name = "probe.txt"
	read_file = open(file_name, 'r')
	
	for line in read_file :
		s = line.split(":")
		if len(s) != 1 :
			movie = s[0]
			input_movies[int(movie)] = 1
			input_users[movie] = []
		else :
			input_users[movie].append(s[0].strip())
	
	for m_id in range (1, 17771) :
		file_name = "/u/downing/cs/netflix/training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		cache = user_ratings_cache(read_file, w, cache, movies, input_users, input_movies)
	
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
		
def user_ratings_cache(r, w, cache, movies, input_users, input_movies) :
	s = "a"
	mov = ""
	flag = 0
	
	ids = -1
	for s in r:
		x = s.split(",")
		ids += 1
		if len(x) == 1 :
			d = s.split(":")
			mov = d[0]
			year = movies[int(mov)]
			if input_movies[int(mov)] == 0 :
				flag = 0
			else :
				flag = 1
			
		else :
			if flag == 1 :
				user_id = x[0]
				movie_users_list = input_users[mov]
				if user_id in movie_users_list :
				
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
							cache[user_id] = user_id_temp
						
						else :
							user_id_temp[year] = [0.0 + int(x[1]), 1.0]
							cache[user_id] = user_id_temp
			
	return cache

# ------
# RMSE
# ------

def create_actual_database(actual) :
	for m_id in range (1, 17771) :
		file_name = "/u/downing/cs/netflix/training_set/mv_"+'%0*d' % (7, m_id)+".txt"
		read_file = open(file_name, 'r')
		for line in read_file :
			s = line.split(",")
			if len(s) == 1 :
				s = line.split(":")
				actual[s[0]] = 0
				movie_id = s[0]
			else :
				d = actual[movie_id]
				user_id = s[0]
				rating = float(s[1])
				if d == 0 :
					d = {user_id:rating}
					actual[movie_id] = d
				else :
					d[user_id] = rating
					actual[movie_id] = d
	
	print actual



# ------
# run
# ------

# cache_start_users(sys.stdout)
#
# or
#
# cache_start_movies

cache_start_users(sys.stdout)



