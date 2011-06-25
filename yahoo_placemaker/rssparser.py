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
from geoplanet import Geoplanet
from textextraction import TermExtractor
from distance import points2distance

class FeedPlace(object):

    def __init__(self, placemakerplace, language='en-US'):
        self.language = language
        self.places = placemakerplace
        geo = Geoplanet(self.language)

        # On définit le lieu le plus probable de la
        # news celui qui a le plus de poids dans le feed
        if len(self.places) != 0:
            max_weight = 0
            for place in self.places:
                print place.name
                print ' longitude : ' , place.centroid.longitude, ' latitude : ', place.centroid.latitude
                if place.weight > max_weight:
                    max_weight = place.weight
                    for place in self.places:
                        if place.weight == max_weight:
                            self.place = place

            # Si le lieu le plus probable est trop étendu, on essaie de trouver
            # dans la liste un lieu descendant de ce dernier
            # -> Le lieu le plus probable devient ce lieu descendant
            if self.place.placetype in ['Continent', 'Supername', 'Colloquial']:
                children = geo.find_children_by_woeid(self.place.woeid, 200)
                children = geo.find_descendants_by_woeid(self.place.woeid)
                for child in children:
                    for place in self.places:
                        if int(child.woeid) == int(place.woeid):
                            self.place = place
                            break
                        break

            # On regarde si il n'y a pas une ville dans la liste dont le
            # parent est le lieu choisi comme étant le plus probable
            # -> Le lieu le plus probable devient cette ville
            for place in self.places:
                if place.placetype in ['Town', 'Local Administrative Area', 'County', 'State', 'Province', 'Prefecture', 'Region', 'Federal District', 'Department', 'District', 'Commune', 'Municipality', 'Ward']:
                    country_related = geo.find_places_by_name(place.name[-2:])
                    try :
                        if int(country_related[0].woeid) == int(self.place.woeid):
                            self.place = place
                            #print place
                    except IndexError:
                        pass

            # On remplit les champs du centroide
            self.latitude = self.place.centroid.latitude
            self.longitude = self.place.centroid.longitude

            # On remplit les informations complémentaires
            self.woeid = self.place.woeid;
            self.placetype = self.place.placetype

        else:
            self.place = 'World'
            self.placetype = 'None'
            self.latitude = 0
            self.longitude = 0
            self.woeid = 0



class Feed(object):

    def __init__(self, title='None', date='None', place='None', description='None', link='None', picture='None', other_links='None', number='None', language='None'):
        self.title = title
        self.date = date
        self.place = place
        self.description = description
        self.link = link
        self.picture = picture
        self.other_links = other_links
        self.number = number
        self.language = language

class RssParser(object):

    def __init__(self, url, language):
        self.language = language
        self.flux = parse(url)
        self.list_feeds = []

    def process(self):
        for i in range(len(self.flux['entries'])):
            feed = Feed(language=self.language)
            p = Placemaker(language=self.language)
            #extractor = TermExtractor()
            feed.title = self.flux.entries[i].title.encode('utf-8', 'ignore')
            feed.date = self.flux.entries[i].date.encode('utf-8', 'ignore')
            feed.number = self.flux.entries[i].guid.split('=')[1]
            feed.description = reduce(lambda x, y: x + y, filter(lambda x: re.match(r'[<>]', x) == None, map(lambda x: re.sub(r'</?(b|font size="-1")>', '', x),re.findall(r'<font size="-1">(.*?)</font>', self.flux.entries[i].description))), '')
            feed.description = feed.description.encode('utf-8', 'ignore')
            #self.subjects = extractor.extraction(feed.description)
            placemaker_place = feed.description + feed.title
            p.find_places(placemaker_place)
            feed.place = FeedPlace(p.places, language=self.language)
            feed.link = re.sub(r'http:(.*?)url=', '', self.flux.entries[i].link)
            feed.link = feed.link.encode('utf-8', 'ignore')
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
            print 'LANGUAGE : %s' % feed.language
            print 'TITLE : %s' % feed.title
            print 'DESCRIPTION : \n %s' % feed.description
            print 'DATE : %s' % feed.date
            print 'PLACES : %s' % feed.place.places
            print 'PLACE TYPE : %s' % feed.place.placetype
            print 'PLACE : %s' % feed.place.place
            print 'COORD : latitude = ' + str(feed.place.latitude) + ' longitude = ' + str(feed.place.longitude)
            print 'WoeID : %s ' % feed.place.woeid
            print 'MAIN LINK : %s' % feed.link
            print 'PICTURE LINK : %s' % feed.picture
            print 'MORE LINKS :'
            for link in feed.other_links:
                print link
            print 'NUMBER : %s' % feed.number
            print
