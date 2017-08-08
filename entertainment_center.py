# -*- coding: cp1252 -*-
import media
import fresh_tomatoes

""" This file specify the name of three moives, a link to movie poster and a 
link to trailor. It then dispalys the movie information on a webpage"""
# specify the first movie's name, link to movie poster, link to movie trailer
hunger_games2015 = media.Movie("Hunger Games: Mockingjay Part 2",
                "A fiction movie of a story of a brave young lady to lead to " + 
                "fight. The movie desmonstrated impressive imaginary future " +
                "technologies.",
                "http://ia.media-imdb.com/images/M/MV5BNjQzNDI2NTU1Ml5BMl5Ban" +
                "BnXkFtZTgwNTAyMDQ5NjE@._V1_SX214_AL_.jpg",
                " https://www.youtube.com/watch?v=3zVaD7t39w8",
                "Jennifer Lawrence",
                "November 16, 2015",
                "PG-13", 
                "https://www.facebook.com/JenniferLawrence",
                "2 hrs. 17 min.")

# print(hunger_games2015.storyline)

# specify the 2nd movie's name, link to the movie poster, link to movie trailer
cinderella_2015 = media.Movie("Cinderella 2015",
                "The real person movie version of Cinderella love story with " +
                "added morden touch.",
                "http://images.mstarz.com/data/images/full/41130/watch-lily-" +
                "james-and-richard-madden-in-2015-cinderella-international-" +
                "movie-trailer-video.jpg?w=600",
                "https://www.youtube.com/watch?v=20DF6U1HcGQ",
                "Lily James",
                "March 6, 2015",
                "PG",
                "https://www.facebook.com/LilyJamesOfficialSite/",
                "1 hrs. 54 min.")

# print(cinderella_2015.storyline)
# cinderella_2015.show_trailer()    

# specify the 3rd movie's name, link to the movie poster, link to movie trailer
taken_3 = media.Movie("Taken 3 (2015)",
        "Bryan has been framed for the murder of his ex-wife. He used his " +
        "unique 007 like skills to clear his name by going after the real " +
        "killer.",
        "https://image.tmdb.org/t/p/original/ikDwR3i2bczqnRf1urJTy77YTFf.jpg",
        "https://www.youtube.com/watch?v=JuU0M2xBasc",
        "Liam Neeson",
        "January 9, 2015",
        "PG-13",
        "https://www.facebook.com/LiamNeesons/",
        "1 hrs. 49 min. ")


# show the movie page with all three movies
movies = [hunger_games2015, cinderella_2015, taken_3]
fresh_tomatoes.open_movies_page(movies)
# below were different tests for calling functions in the Movie class that I 
# did earlier so to use commenting to preservie
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)