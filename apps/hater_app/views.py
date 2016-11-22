from django.shortcuts import render, redirect, HttpResponse
from TwitterSearch import *
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
	consumer_key = 'sKWWP86fBkphMtLTYINRdQ',
	consumer_secret = 'ZdoDvJCzdbZ60y7OPNfLIVtcdhE',
    token = 'hF6LiItqZwotEi-pZghzcxLsGf1N3p5P',
    token_secret = 'ETi02p-5lO2hKM5bBACayb-cX_w'
)
client = Client(auth)


def index(request):
    context = {
        'hello' : 'Hello World!'
    }
    return render(request, 'hater_app/index.html', context)


def search(request):
	if request.method == "POST":
		latitude = float(request.POST['lati'])
		longitude = float(request.POST['longi'])
		params = {
			'sort_by' : 'rating',
			'term' : 'pizza',
			'lang' : 'en',
			'radius_filter' : 2000
		}
		response = client.search_by_coordinates(latitude, longitude, **params)
	context = {
				'businesses' : response.businesses
	}
	return render(request, 'hater_app/index.html', context)
