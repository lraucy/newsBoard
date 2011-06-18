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
import re
from feedparser import parse
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

class PlacemakerPlace(object):

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
            feed.picture = temp[0]
            feed.other_links = [url for url in map(lambda x: re.sub(r'http:(.*?)url=', '', x), re.findall(r'<a href="([^"]*)">', self.flux.entries[i].description.encode('utf-8', 'ignore')))]
            self.list_feeds.append(feed)
        return self.list_feeds

    def print_feeds(self):
        for feed in self.list_feeds:
            print 'TITLE : %s' % feed.title
            print 'DESCRIPTION : \n %s' % feed.description
            print 'DATE : %s' % feed.date
            print 'PLACES : %s' % feed.place.places
            print 'PLACE DEF : %s' % feed.place.place
            print 'COUNTRY : %s' % feed.place.countrie
            print 'CITY : %s' % feed.place.city
            print 'COORD : latitude = ' + str(feed.place.latitude) + ' longitude = ' + str(feed.place.longitude)
            print 'MAIN LINK : %s' % feed.link
            print 'PICTURE LINK : %s' % feed.picture
            print 'MORE LINKS :'
            for link in feed.other_links:
                print link
            print


class Placemaker(object):

    def find_places(self, documentContent = 'None', documentType='text/plain', inputLanguage='en-US',
                    outputType='xml', documentTitle='', autoDisambiguate='true',
                    focusWoeid=''):

        self.values = {'appid': API_KEY,
                       'documentType': documentType,
                       'inputLanguage': inputLanguage,
                       'documentContent': documentContent,
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
        self.places = [PlacemakerPlace(place) for place in place_details]
        return self.places


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:


