import Media
import fresh_tomatoes

toy_story = Media.Movie('Toy Story', 'This is story about the toy and boy',
                    'https://en.wikipedia.org/wiki/File:Toy_Story.jpg',
                    'https://www.youtube.com/watch?v=x2xaLGOE5NY&list=RDMMx2xaLGOE5NY')

# toy story
#print(toy_story.storyline)

# open the show trailer
#print(toy_story.show_trailer())

# movies = [toy_story]

# print(fresh_tomatoes.open_movies_page(movies))

# let me print the class variables
# print(Media.Movie.VALID_RATING)

# Print the doc statment the movie.
print(Media.Movie.__doc__) # doc string of the class

print(Media.Movie.__name__) # Name of the class

print(Media.Movie.__module__) # Module is the media. the file where we have written the module-inside will be the class


