from django.shortcuts import render, redirect, HttpResponse
from TwitterSearch import *
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import requests


auth = Oauth1Authenticator(
	consumer_key = 'sKWWP86fBkphMtLTYINRdQ',
	consumer_secret = 'ZdoDvJCzdbZ60y7OPNfLIVtcdhE',
    token = 'hF6LiItqZwotEi-pZghzcxLsGf1N3p5P',
    token_secret = 'ETi02p-5lO2hKM5bBACayb-cX_w'
)
client = Client(auth)


def index(request):
    return render(request, 'hater_app/index.html')


def search(request):
	if request.method == "POST":

		latitude = float(request.POST['lati'])
		longitude = float(request.POST['longi'])
		if latitude not in request.session:
			request.session['latitude'] = latitude
			request.session['longitude'] = longitude

		terms = request.POST['term']
		split_terms = terms.split(',')
		search_terms = ''
		print len(split_terms)
		for term in split_terms:
			search_terms += str(term)+','

		params = {
			'sort_by'       : 'rating',
			'term'          : search_terms,
			'lang'          : 'en',
			'radius_filter' : 2000
		}
		# Yelp call
		response = client.search_by_coordinates(latitude, longitude, **params)
		print ('response', response, 'response.businesses', response.businesses)

		businesses = [];
		# Keep only the suck
		for business in response.businesses:
			if business.rating <= 3:
				businesses.append(business)

	context = {
		'businesses' : businesses,
		'terms'      : request.POST['term'],
		'suck'       : len(businesses)
	}
	return render(request, 'hater_app/index.html', context)


def result_disp(request):
	post           = request.POST
	latitude       = post['latitude']
	longitude      = post['longitude']
	address        = post['address']
	city           = post['city']
	name           = post['name']
	review_count   = post['review_count']
	displayaddress = post['displayaddress']
	img_rating     = post['img_rating']
	totaladd       = address + ' ' + city
	newadd         = ""

	for i in range (0, len(totaladd)):
		if totaladd[i] == ' ':
			newadd += '+'
		else:
			newadd += totaladd[i]

	completeadd = "https://www.google.com/maps/embed/v1/directions?key=AIzaSyA8kcACFywGgMzo59IA8vov0zF1u78f11A&origin=" + str(post['lati']) + "," + str(post['longi']) + "&destination=" + newadd + "&mode=driving"
	context = {
		'latitude'       : latitude,
		'longitude'      : longitude,
		'completeadd'    : completeadd,
		'img_rating'     : img_rating,
		'name'           : name,
		'review_count'   : review_count,
		'displayaddress' : totaladd
	}
	return render(request, 'hater_app/results.html', context)

