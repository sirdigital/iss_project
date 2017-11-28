import urllib.request, json
import threading
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_long_lat():

	'''
	Load ISS position data
	:return: longitude, latitude dictionary
	'''

	with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as url:
		data = json.loads(url.read().decode())
		return(data["iss_position"])

def draw_position():

	'''
	Transforms current position of ISS to pixel values and draws it on the map
	'''

	dict = get_long_lat()

	lat_in_px = 69.0 + (float(dict["latitude"]) + 90) * 10.6
	long_in_px = 39.0 + (float(dict["longitude"]) + 180) * 10.6

	plt.scatter(x=long_in_px, y=lat_in_px, c="r", s=60)

	plt.draw()

def position_every_second():

	'''
	Starts a thread activating draw_position() method every 0.5 second
	'''

	threading.Timer(0.5, position_every_second).start()
	draw_position()

img = plt.imread("world.jpg")
fig, ax = plt.subplots()

ax.imshow(img, extent=[0, 3900, 0, 1820])

dict = get_long_lat()

plt.ion()

position_every_second()

plt.show(block=True)