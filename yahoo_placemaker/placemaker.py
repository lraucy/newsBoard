#!/usr/bin/python2
# -*-coding:Utf-8 -*

"""
Python wrapper for the Yahoo Placemaker API.

Requires Python 2.5 or above.

Requires an API key from the Yahoo Developer network:
https://developer.yahoo.com/wsregapp/

See also:

Yahoo Placemaker API Documentation:
http://developer.yahoo.com/geo/placemaker/guide/api_docs.html

Yahoo Placemaker API Reference:
http://developer.yahoo.com/geo/placemaker/guide/api-reference.html
"""

__author__ = "Aaron Bycoffe (bycoffe@gmail.com)"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2009 Aaron Bycoffe"
__license__ = "BSD"


import urllib
import urllib2
import feedparser
from xml.etree import ElementTree

# When using ElementTree to parse the XML returned by the API,
# each tag is prefixed by the schema URL. We need to use this
# prefix when finding tags in the document.
TAG_PREFIX = '{http://wherein.yahooapis.com/v1/schema}'
# API Key to be able tu use Yahoo PlaceMaker
API_KEY = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
# Yahoo PlaceMaker API URL
API_URL = 'http://wherein.yahooapis.com/v1/document'
#URL_SOURCE = 'http://rss.news.yahoo.com/rss/topstories'

class Place(object):

    def __init__(self, tree):
        self.place = tree.find('%splace' % TAG_PREFIX)

        self.woeid = self.place.find('%swoeId' % TAG_PREFIX).text
        try:
            self.woeid = int(self.woeid)
        except ValueError:
            pass

        self.placetype = self.place.find('%stype' % TAG_PREFIX).text
        self.name = self.place.find('%sname' % TAG_PREFIX).text
        self.name = self.name.encode('utf-8', 'ignore')

        self.centroid = PlacemakerPoint(self.place.find('%scentroid' % TAG_PREFIX))
        self.match_type = tree.find('%smatchType' % TAG_PREFIX).text
        try:
            self.match_type = int(self.match_type)
        except ValueError:
            pass

        self.weight = tree.find('%sweight' % TAG_PREFIX).text
        try:
            self.weight = int(self.weight)
        except ValueError:
            pass

        self.confidence = tree.find('%sconfidence' % TAG_PREFIX).text
        try:
            self.confidence = int(self.confidence)
        except ValueError:
            pass

    def __repr__(self):
        return self.name

class PlacemakerPoint(object):

    def __init__(self, tree):
        self.latitude = tree.find('%slatitude' % TAG_PREFIX).text
        if self.latitude:
            self.latitude = float(self.latitude)

        self.longitude = tree.find('%slongitude' % TAG_PREFIX).text
        if self.longitude:
            self.longitude = float(self.longitude)

    def __repr__(self):
        return u"<Placemaker Point: '%s, %s'>" % (self.latitude, self.longitude)

class placemaker(object):


    def __init__(self, url):
        self.flux = feedparser.parse(url)
        self.titles = []
        self.links = []
        self.dates = []
        self.descriptions = []
        self.places = []
        self.longitudes = []
        self.latitudes = []
        self.places_def = []

    def find_places(self, input, documentType='text/plain', inputLanguage='en-US',
                    outputType='xml', documentTitle='', autoDisambiguate='true',
                    focusWoeid=''):

        self.values = {'appid': API_KEY,
                       'documentType': documentType,
                       'inputLanguage': inputLanguage,
                       'documentContent': input,
                       'outputType': outputType,
                       'documentTitle': documentTitle,
                       'autoDisambiguate': autoDisambiguate,
                       'focusWoeid': focusWoeid, }

        self.data = urllib.urlencode(self.values)
        self.req = urllib2.Request(API_URL, self.data)
        self.response = urllib2.urlopen(self.req)

        response_codes = {400: 'Bad Request',
                          404: 'Not Found',
                          413: 'Request Entity Too Large',
                          415: 'Unsupported Media Type',
                          999: 'Unable to process request at this time', }

        if self.response.code != 200:
            raise PlacemakerApiError('Request received a response code of %d: %s' % (self.response.code, response_codes[self.response.code]))

        self.response_xml = self.response.read()

        self.tree = ElementTree.fromstring(self.response_xml)

        self.doc = self.tree.find('%sdocument' % TAG_PREFIX)

        place_details = self.doc.findall('%splaceDetails' % TAG_PREFIX)
        list_places = [Place(place) for place in place_details]
        return list_places


    def process(self):
        for i in range(len(self.flux['entries'])):
            self.titles.append(self.flux.entries[i].title)
            self.links.append(self.flux.entries[i].link)
            self.dates.append(self.flux.entries[i].date)
            self.descriptions.append(self.flux.entries[i].description)
            self.places.append(self.find_places(self.descriptions[i].encode('utf-8', 'ignore')))

        for location in self.places:
            max_weight = 0
            if location != []:
                for place in location:
                    if place.weight > max_weight:
                        max_weight = place.weight

                for place in location:
                    if place.weight == max_weight:
                        self.places_def.append(place)
                        self.longitudes.append(place.centroid.longitude)
                        self.latitudes.append(place.centroid.latitude)
                        break
            else:
                self.places_def.append("World")
                self.longitudes.append(0)
                self.latitudes.append(0)

    def print_locations(self):
        for i in range(len(self.titles)):
            print 'FEED NUMBER : %d' % (i+1)
            print 'TITLE : %s' % self.titles[i]
            print 'DATE : %s' % self.dates[i]
            print 'PLACES : %s' % self.places[i]
            print 'PLACES DEF : %s' % self.places_def[i]
            print 'COORD : latitude = ' + str(self.latitudes[i]) + ' longitude = ' + str(self.longitudes[i])
            print



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
