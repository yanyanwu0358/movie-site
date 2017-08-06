# -*- coding: cp1252 -*-
import webbrowser

class Movie():
	""" This class provides a way to store movie """
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self,movie_title,movie_storyline,post_image,trailer_youtube,actor,theater_release_date,movie_rating,facebook_link):
		self.title=movie_title
		self.storyline= movie_storyline
		self.poster_image_url= post_image
		self.trailer_youtube_url= trailer_youtube
		self.actor_name=actor
		self.release_date=theater_release_date
		self.rating=movie_rating
		self.actor_facebook=facebook_link

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
