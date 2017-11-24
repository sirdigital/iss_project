import urllib.request, json
import threading
from turtle import *
import turtle
from tkinter import *

def get_long_lat():
	with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as url:
		data = json.loads(url.read().decode())
		print(data["iss_position"])

def position_every_second():
	threading.Timer(0.5, position_every_second).start()
	get_long_lat()


screen = Screen()

screen_x, screen_y = screen.screensize()

screen.bgpic("world.jpg")

screen.bgpic()

# position_every_second()