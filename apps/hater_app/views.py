from django.shortcuts import render, redirect, HttpResponse

from TwitterSearch import *


def index(request):
    context = {
        'hello' : 'Hello World!'
    }
    return render(request, 'hater_app/index.html', context)

def search_twitter(request):
    latitude = float(request.POST['lati'])
    longitude = float(request.POST['longi'])
    print "Hello"
    print latitude
    print longitude
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(['hate', 'OR', 'sucks']) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = 'elkX0qShud5aUu10lkyF7Q3mt',
            consumer_secret = 'CeQHBJbq7T5Cz0dl1oKlSAJFwTrzyJVjNbtsu0BHhoshGl2Y5y',
            access_token = '800796532890947585-KAxs6wDlGD42CZm2v2TmRTo6f7eezD4',
            access_token_secret = 'xrwjSGbN7NtsaDRtIUnWFAguLsARzV1fTAdwNjsmKWwIp'
        )
        tso.set_geocode(latitude,longitude,200,imperial_metric=True)
        # this is where the fun actually starts :slightly_smiling_face:
        for tweet in ts.search_tweets_iterable(tso):
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)
    return redirect('/')

