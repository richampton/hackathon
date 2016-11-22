from django.shortcuts import render, redirect, HttpResponse
from TwitterSearch import *
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


auth = Oauth1Authenticator(
	consumer_key = sKWWP86fBkphMtLTYINRdQ,
	consumer_secret = ZdoDvJCzdbZ60y7OPNfLIVtcdhE,
    token = hF6LiItqZwotEi-pZghzcxLsGf1N3p5P,
    token_secret = ETi02p-5lO2hKM5bBACayb-cX_w
)
client = Client(auth)


def index(request):
    context = {
        'hello' : 'Hello World!'
    }
    return render(request, 'hater_app/index.html', context)


def search(request):
	if request.method == "POST":
		params = {
			'term': 'pizza',
			'lang': 'en'
		}
		response = client.search('San Jose', **params)
		print response.businesses[0].name
		print response.businesses[1].name
		print response.businesses[2].name

	    return redirect('/')

