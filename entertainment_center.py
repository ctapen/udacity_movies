import fresh_tomatoes
import media


# Create instances of Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

BILB = media.Movie("Bend It Like Beckham",
                   "An indian girl living in UK who just wants to play football.",
                   "https://upload.wikimedia.org/wikipedia/en/1/1c/Bend_It_Like_Beckham_movie.jpg",
                   "https://www.youtube.com/watch?v=Z7Pt_GMDdGo")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatoille", "A rat is a chef in Paris.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games", "A really real reality show.",
                                "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                                "https://www.youtube.com/watch?v=4S9a5V9ODuY")

# Make a list of Movies
movies = [toy_story, avatar, BILB, school_of_rock, ratatouille, hunger_games]
# print(movies)

# Display these movies on a webpage
fresh_tomatoes.open_movies_page(movies)

# Print ratings or documentation
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
