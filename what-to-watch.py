import csv
​
"""We want to make this data structure much more managble. We can create lists and dictionaries
to pile this data into more effective ways to navigate. The user has access to the movie_id, but
what can he do it with?

By using the move_id, the user should be able to pull up the AVERAGE rating for that movie, which
is computed using the (Sum(Total Ratings/movie)/(total amount of times that movie was reviewed)). The movies need to
be sorted into lists per genre based on the info from the data.(how would you determine what movie is what type?)
Once we have the average rating/movie we can use the top 20 averages/genre to recommend movies based
on the user's input("What genre of movie would you like to watch?"); should print(a dictionary of the genre)
so user can select a keyword(number) and the value(genre type) would be returned. By selecting the keyword
the computer returns the top 20 movies per that genre. THEN, with the dictionary of the top 20, keyword(position)
and value(movie title), the user input returns the movie and the average rating."""



genre = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary',
'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi'
'Thriller', 'War', 'Western']


class Movie:
	"""What are the attributes that will help us make a dictionary that allows
	us to correlate the movie_id to the movie title? Also, include the genre so
	user can search by genre and we can return the top 20 rated movies per genre"""
	def __init__(self, movie_id, title, genre):
		self.id = movie_id
		self.title = title
    	self.genre = genre
​
	def __str__(self):
		return '{}: {}'.format(self.id, self.title)


class Ratings:
	"""What are the attributes that the ratings are composed of that will help
	us make a recommendation? We need to find the total amount of reviews per movie
	and also the average review per movie"""
	def __init__(self, movie_id, review):
		self.movie_id = movie id
		self.rating = review

	def __str__(self):
		"""not sure if this is going to work; I'm trying to TAKE the movie title
		from the movie{} and ADD it to the rating {}.
		the movie_id is the movie title from the movies dictionary
		{movie_id: movie title}"""
		return '{}: {}'.format(self.rating, self.movie_id)


class User:
	"""Lets see what every user has in common that would be beneficial in helping
	to make a recommendation to another user"""
	def __init__(self, user_id, age, gender, occupation):
		self.user_id = user_id
		self.age = age
		self.gender = gender
		self.occupation = occupation

	def __str__(self):
		return

"""by making a dictionary of the movies, we can search by movie_id or the title
of the movie"""​
movies = {}
​
"""this opens the document with the pertient info about the movie title and its
respective movie_id. Once we extract the movie title from the data, we can find
the total amount of reviews of that movie, which will aid us in finding the average
review of said movie."""
with open('u.item', encoding='latin_1') as item_file:
	reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
	for row in reader:
    # this is going to create a dictionary with the 'movie_id' as the keyword
    # and the 'title' as the value.
		movie = Movie(row['movie_id'], row['title'])
		movies[movie.id] = movie
​
"""by putting the movies in a list, we might be able to loop over the list better
just to find the titles easier."""
movies_list = [movies[key] for key in movies]
​











# user_input = input('Enter part of a movie title: ').lower()
# ​
# for movie in movies_list:
# 	if user_input in movie.title.lower():
# 		print(movie)
# ​
# id = input('Enter a movie id: ')
# ​
# do something with id, like look up the movie in the movies dictionary and print out the ratings for that movie, then prompt the user for input again if they want to find similar movies, etc.. etc..
