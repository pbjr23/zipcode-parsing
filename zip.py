#!/bin/env python3.3

from bs4 import BeautifulSoup
import urllib2
# import pprint

data = {}

def init_fetch(zipcode):
	# Opens the source of the url and soupifies it	
	url = "http://www.uszip.com/zip/" + str(zipcode)	
	url = urllib2.urlopen(url)
	content = url.read()
	soup = BeautifulSoup(content)
	

def listify(n):
	"""
	returns the food options for each category of food
	eg: for "Comfort" it might return
	     ["onion rings", "bread", "cheese"]
	"""
	raw = n.next_sibling.next_sibling.getText()
	output_list = raw.split("\n")
	output_list = [_f for _f in output_list if _f]
	return output_list


def get_city_state():
	"""
	Returns a list containing city and state.
	Eg: ["Northville", "MI"]
	"""
	# first tag with h2 is the City, State
	headers_raw = soup.findAll("h2")
	return headers_raw[0].getText().split(",")

def get_population_data():



	# Creates master vegetarian dictionary
	# all_dict = {}
	# # For loop to create veg_dict
	# for raw_header in headers_raw:
	# 	header_title = raw_header.getText()
	# 	temp = {}
	# 	# "strong" finds all the categories
	# 	for category in raw_header.next_sibling.findAll("strong"):
	# 		categoryText = category.getText()
	# 		temp[categoryText] = listify(category)
	# 	all_dict[header_title] = temp
	# return all_dict

print get_city_state(48167)

def get_veg_meals(url):
	"""
	Prints out a dictionary of all the vegetarian meals.
	"""

	# Opens the source of the url and soupifies it
	url = urllib.request.urlopen(url)
	content = url.read()
	soup = BeautifulSoup(content)
	# Finds all tags with h4 (LUNCH, DINNER, etc)
	headers_raw = soup.findAll("h4")
	# Creates master vegetarian dictionary
	veg_dict = {}
	# For loop to create veg_dict
	for raw_header in headers_raw:
		header_title = raw_header.getText()
		temp = {}
		# "strong" finds all the categories
		for category in raw_header.next_sibling.findAll("strong"):
			categoryText = category.getText()
			temp[categoryText] = veg_listify(category)
		veg_dict[header_title] = temp

# print all_dict
# pp = pprint.PrettyPrinter(indent = 2)
# pp.pprint(get_all_meals("http://cms.business-services.upenn.edu/dining/hours-locations-a-menus/residential-dining/hill-house/daily-menu.html"))
