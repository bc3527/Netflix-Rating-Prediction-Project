### Cache maker
### RMSE

# Imports #

import sys

# ------
# RMSE
# ------
def RMSE_start() :
	prediction = {}
	a = create_prediction_database(prediction)
	prediction = a[0]
	movies = a[1]
	users = a[2]
	actual = {}
	actual = create_actual_database(actual, movies, users, prediction)


def create_actual_database(actual, movies, users, prediction) :
	i = [1.0]
	x = [0.0]
	#print movies
	file_name = "limitedActual.txt"
	read_file = open(file_name, 'r')
	for line in read_file :
		s = line.split(",")
		if len(s) == 1 :
			s = line.split(":")
			m = s[0]
			p = prediction[m]
		else :
			#d = actual[m]
			user_id = s[0]
			Arating = float(s[1])
			Prating = p[user_id]
			assert type(Prating) is float
			x[0] += sqre_diff(Arating, Prating)
			i[0] += 1
	
	count = i[0] - 1
	total = x[0]
	RMSE = total/count					
	print "RMSE = " + str(RMSE)
	

def create_prediction_database(prediction) :
	file_name = "probePrediction.txt"
	read_file = open(file_name, 'r')
	movies = [0]*17771
	users = [0]*17771
	for line in read_file :
		s = line.split(",")
		if len(s) == 1 :
			s = line.split(":")
			prediction[s[0]] = 0
			movie_id = s[0]
			movies[int(movie_id)] = 1
			users[int(movie_id)] = []
		else :
			d = prediction[movie_id]
			user_id = s[0]
			users[int(movie_id)].append(user_id)
			rating = float(s[1])
			if d == 0 :
				d = {user_id:rating}
				prediction[movie_id] = d
			else :
				d[user_id] = rating
				prediction[movie_id] = d

	return [prediction, movies, users]

def sqre_diff (x, y) :
	return (x - y) ** 2	

# ------
# run
# ------

RMSE_start()
