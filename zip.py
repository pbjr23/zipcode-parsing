from bs4 import BeautifulSoup
import urllib2
import re
# import pprint

data = {}

def init_fetch(zipcode):
	# Opens the source of the url and soupifies it
	# soup contains the source code of the page 
	global soup
	url = "http://www.uszip.com/zip/" + str(zipcode)	
	url = urllib2.urlopen(url)
	content = url.read()
	soup = BeautifulSoup(content)
	

def get_city_state():
	"""
	Returns a list containing city and state.
	Eg: ["Northville", "MI"]
	"""
	# first tag with h2 is the City, State
	headers_raw = soup.findAll("h2")
	return headers_raw[0].getText().split(",")

def get_population_data():
	"""
	<dt>Land area<br><span class="stype">(sq. miles)</span></dt>
	        <dd>17.78</dd>
	"""
	population = {}
	population["total"] = soup.find("dt",text="Total population").next_sibling.contents[0]
	population["housing_units"] = soup.find("dt",text="Housing units").next_sibling.contents[0]
	# Note: land_area and water_area are in square miles
	population["land_area"] = soup.find("dt",text=re.compile("Land area")).contents[0]

	# for i in bob:
		# print i.getText()
	# population["water_area"] = soup.find("dt",text="Water area").next_sibling.contents[0]
	return population

init_fetch(48167)
print get_city_state()
print get_population_data()
