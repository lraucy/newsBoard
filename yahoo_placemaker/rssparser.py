#!/usr/bin/python2
# -*-coding:Utf-8 -*

# When using ElementTree to parse the XML returned by the API,
# each tag is prefixed by the schema URL. We need to use this
# prefix when finding tags in the document.
TAG_PREFIX = '{http://wherein.yahooapis.com/v1/schema}'
# API Key to be able tu use Yahoo PlaceMaker
API_KEY = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
# Yahoo PlaceMaker API URL
API_URL = 'http://wherein.yahooapis.com/v1/document'


import re
from feedparser import parse
from placemaker import Placemaker

class FeedPlace(object):

    def __init__(self, placemakerplace):
        self.places = placemakerplace
        # Liste des lieux présents dans la news
        if len(self.places) != 0:
            max_weight = 0
            for place in self.places:
                if place.weight > max_weight:
                    max_weight = place.weight
                    # Lieu de la news comme étant le plus probable
                    for place in self.places:
                        if place.weight == max_weight:
                            self.place = place

            self.latitude = self.place.centroid.latitude
            self.longitude = self.place.centroid.longitude

            self.woeid = self.place.woeid;
            self.placetype = self.place.placetype

            # Le nom de la ville et du pays associés
            if self.place.placetype == 'Town':
                temp = re.findall(r'[A-Z][A-Z]', self.place.name)
                self.countrie = temp[0]
                temp = re.findall(r'^(.*?),', self.place.name)
                self.city = temp[0]
            else:
                self.countrie = self.place.name
                self.city = 'None'
        else:
            self.place = "World"
            self.latitude = 0
            self.longitude = 0
            self.countrie = 'All'
            self.city = 'All'
            self.woeid = 0


class Feed(object):

    def __init__(self, title='None', date='None', place='None', description='None', link='None', picture='None', other_links='None'):
        self.title = title
        self.date = date
        self.place = place
        self.description = description
        self.link = link
        self.picture = picture
        self.other_links = other_links

class RssParser(object):

    def __init__(self, url):
        self.flux = parse(url)
        self.list_feeds = []

    def process(self):
        for i in range(len(self.flux['entries'])):
            feed = Feed()
            p = Placemaker()
            feed.title = self.flux.entries[i].title
            feed.date = self.flux.entries[i].date
            p.find_places(self.flux.entries[i].description.encode('utf-8', 'ignore'))
            feed.place = FeedPlace(p.places)
            feed.description = reduce(lambda x, y: x + y, filter(lambda x: re.match(r'[<>]', x) == None, map(lambda x: re.sub(r'</?(b|font size="-1")>', '', x),re.findall(r'<font size="-1">(.*?)</font>', self.flux.entries[i].description.encode('utf-8', 'ignore')))), '')
            feed.link = re.sub(r'http:(.*?)url=', '', self.flux.entries[i].link)
            temp = re.findall(r'src="([^"]*)"', self.flux.entries[i].description.encode('utf-8', 'ignore'))
            if len(temp) != 0:
                feed.picture = temp[0]
            else:
                feed.picture = 'None'
            feed.other_links = [url for url in map(lambda x: re.sub(r'http:(.*?)url=', '', x), re.findall(r'<a href="([^"]*)">', self.flux.entries[i].description.encode('utf-8', 'ignore')))]
            self.list_feeds.append(feed)
        return self.list_feeds

    def print_feeds(self):
        for feed in self.list_feeds:
            print 'TITLE : %s' % feed.title
            print 'DESCRIPTION : \n %s' % feed.description
            print 'DATE : %s' % feed.date
            print 'PLACES : %s' % feed.place.places
            print 'PLACE TYPE : %s' % feed.place.placetype
            print 'PLACE DEF : %s' % feed.place.place
            print 'COUNTRY : %s' % feed.place.countrie
            print 'CITY : %s' % feed.place.city
            print 'COORD : latitude = ' + str(feed.place.latitude) + ' longitude = ' + str(feed.place.longitude)
            print 'WoeID : %s ' % feed.place.woeid
            print 'MAIN LINK : %s' % feed.link
            print 'PICTURE LINK : %s' % feed.picture
            print 'MORE LINKS :'
            for link in feed.other_links:
                print link
            print
