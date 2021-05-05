import tweepy
from PIL import Image, ImageColor
from io import BytesIO
from config import *
import random
import time


class ColourBot(object):

	def __init__(self):

		auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY) #You'll need to get these from developers.twitter.com

		auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET) 

		self.bot = tweepy.API(auth)


	def start(self,delay= 300):
		'''Starts our Tweet loop'''
		while True:
			self.tweet_random_color()
			time.sleep(delay)


	def tweet_random_color(self):
		'''Posts a random color to the bot's twitter timeline'''


		color = '#'+ str(hex(random.randint(0,0xFFFFFF)))[2:] #Get a random color code. Note that this isn't always valid
		
		try:
			rgb = ImageColor.getrgb((color))
		except ValueError: #This is raised when the hex color code is invalid
			return self.tweet_random_color()

		img = Image.new('RGB', (1920, 1920), rgb)


		with BytesIO() as BIO: 
			img.save(BIO,'PNG')
			BIO.seek(0) #Copy pasted code from R. Twinkle's color extension XD


			media = self.bot.media_upload(filename=f'{color}.png',file=BIO)
			tweet= self.bot.update_status(status=f'{color} {rgb}',media_ids=[media.media_id])
			#twitter.com/TheColourBot
			
			print('Tweeted!') #Just to make sure everything is fine


bot = ColourBot()
bot.start()