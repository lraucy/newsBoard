#!/usr/bin/env python
# -*- coding: utf-8 -*-

# When using ElementTree to parse the XML returned by the API,
# each tag is prefixed by the schema URL. We need to use this
# prefix when finding tags in the document.
TAG_PREFIX = '{http://wherein.yahooapis.com/v1/schema}'
# API Key to be able tu use Yahoo PlaceMaker
API_KEY = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
# Yahoo PlaceMaker API URL
API_URL = 'http://wherein.yahooapis.com/v1/document'



import re
import sys
from feedparser import parse
from placemaker import Placemaker
from geoplanet import Geoplanet
from textextraction import TermExtractor
from pyproj import Geod

class FeedPlace(object):

    def __init__(self, placemakerplace, lang='en-US'):
        self.lang = lang
        self.places = placemakerplace
        geo = Geoplanet(self.lang)
        geod = Geod(ellps='WGS84')

        # Si la liste des lieux est vide, on élimine la
        # news
        if len(self.places) != 0:

            # On définit le lieu le plus probable de la
            # news celui qui a le plus de poids dans le feed
            max_weight = 0
            for place in self.places:
                if place.weight > max_weight:
                    max_weight = place.weight
            for place in self.places:
                if place.weight == max_weight:
                    self.place = place
                    break


            # On cherche dans la liste si il n'y a pas un lieu
            # de même poids que le lieu choisi comme étant le plus probable
            # On regarde ensuite si ce lieu est très éloigné, si oui
            # on élimine la news car pas assez d'info significative
            max_dist = 2000
            news_invalid = False
            for place in self.places:
                if place.woeid != self.place.woeid:
                    if place.weight == self.place.weight:
                        az12, az21, dist = geod.inv(self.place.centroid.longitude, self.place.centroid.latitude, place.centroid.longitude, place.centroid.latitude)
                        dist = int(dist / 1000)
                        if dist > max_dist:
                            news_invalid = True


            # Si le lieu le plus probable est trop étendu, on essaie de trouver
            # dans la liste un lieu descendant de ce dernier
            # -> Le lieu le plus probable devient ce lieu descendant
            if self.place.placetype in ['Continent', 'Supername']:
                children = geo.find_children_by_woeid(self.place.woeid, 200)
                #children = geo.find_descendants_by_woeid(self.place.woeid)
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
                    except IndexError:
                        pass


            # On cherche la distance maximale entre deux lieux dans la news
            # Ca sert plus à grand chose
            max_dist = 0
            place_temp = self.places[:]
            while (len(place_temp) != 1):
                for place in place_temp[1:]:
                    if place_temp[0].weight == place.weight:
                        az12, az21, dist = geod.inv(place_temp[0].centroid.longitude, place_temp[0].centroid.latitude, place.centroid.longitude, place.centroid.latitude)
                        if dist > max_dist:
                            max_dist = dist
                place_temp.pop(0)
            self.max_dist = int(max_dist / 1000)

            # On remplit les champs du centroide
            self.latitude = self.place.centroid.latitude
            self.longitude = self.place.centroid.longitude

            # On remplit les informations complémentaires
            self.woeid = self.place.woeid;
            self.placetype = self.place.placetype

            if news_invalid:
                self.place = 'World'
                self.placetype = 'None'
                self.latitude = 0
                self.max_dist = 0
                self.longitude = 0
                self.woeid = 0

        else:
            self.place = 'World'
            self.placetype = 'None'
            self.latitude = 0
            self.max_dist = 0
            self.longitude = 0
            self.woeid = 0


class Feed(object):

    def __init__(self, title='None', date='None', place='None', description='None', link='None', picture='None', other_links='None', number='None', lang='None',lang_place='None', max_dist='None', date_parsed='None', topic='None', source='None'):
        self.title = title
        self.date = date
        self.date_parsed = date_parsed
        self.place = place
        self.description = description
        self.link = link
        self.picture = picture
        self.other_links = other_links
        self.number = number
        self.lang = lang
        self.lang_place = lang_place
        self.topic = topic
        self.source = source


class RssParser(object):

    def __init__(self, url):
        self.url = url
        self.lang, self.lang_place, self.topic = parse_url(self.url)
        self.flux = parse(self.url)
        self.list_feeds = []

    def process(self):
        for i in range(len(self.flux['entries'])):
            feed = Feed(lang=self.lang, lang_place=self.lang_place, topic=self.topic)
            p = Placemaker(lang=self.lang_place)
            feed.title, feed.source = parse_title(self.flux.entries[i].title.encode('utf-8', 'ignore'))
            feed.date = self.flux.entries[i].date.encode('utf-8', 'ignore')
            feed.date_parsed = self.flux.entries[i].updated_parsed
            feed.number = self.flux.entries[i].guid.split('=')[1]
            feed.description = clear_text(self.flux.entries[i].description)
            placemaker_place = feed.description + feed.title
            p.find_places(placemaker_place)
            feed.place = FeedPlace(p.places, lang=self.lang_place)
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
            print 'LANG : %s' % feed.lang
            print 'LANG_PLACE : %s' % feed.lang_place
            print 'TOPIC : %s' % feed.topic
            print 'TITLE : %s' % feed.title
            print 'SOURCE : %s' % feed.source
            print 'DESCRIPTION : \n %s' % feed.description
            print 'DATE : %s' % feed.date
            print 'YEAR : %s' % feed.date_parsed.tm_year
            print 'PLACES : %s' % feed.place.places
            print 'PLACE TYPE : %s' % feed.place.placetype
            print 'PLACE : %s' % feed.place.place
            print 'DISTANCE MAX : %s' % feed.place.max_dist
            print 'COORD : latitude = ' + str(feed.place.latitude) + ' longitude = ' + str(feed.place.longitude)
            print 'WoeID : %s ' % feed.place.woeid
            print 'MAIN LINK : %s' % feed.link
            print 'PICTURE LINK : %s' % feed.picture
            print 'MORE LINKS :'
            for link in feed.other_links:
                print link
            print 'NUMBER : %s' % feed.number
            print

def clear_text(text='None'):
    temp =  reduce(lambda x, y: x + y, filter(lambda x: re.match(r'[<>]', x) == None, map(lambda x: re.sub(r'</?(b|font size="-1")>', '', x),re.findall(r'<font size="-1">(.*?)</font>', text))), '')
    return temp.encode('utf-8')

def parse_url(url='None'):
    split_url = url.split('&')
    language = split_url[2][4:]
    lang = dico_lang[language]
    lang_place = dico_lang_place[language]

    if split_url[4].find('output') != -1:
        topic = 'starred'
    else:
        topic = split_url[4][6:]
        topic = dico_topic[topic]

    return lang, lang_place, topic

def parse_title(title='None'):
    title_split = title.split('-')
    source = title_split[len(title_split)-1]
    source = source[1:]
    title = title[:len(title)-len(source)-3]
    return title, source

dico_topic = {'w' : 'news',
              'n' : 'news',
              'af' : 'news',
              'se' : 'news',
              'b' : 'business',
              't' : 'science/tech',
              's' : 'sport',
              'm' : 'health',
              'ir' : 'spotlight',
              'po' : 'spotlight',
              }

dico_lang_place = {'fr' : 'fr-FR',
                   'fr_ch' : 'fr-FR',
                   'fr_sn' : 'fr-FR',
                   'fr_ca' : 'fr-CA',
                   'fr_be' : 'fr-FR',
                   'es' : 'es-ES',
                   'es_ve' : 'es-ES',
                   'es_pe' : 'es-ES',
                   'es_mx' : 'es-MX',
                   'es_us' : 'es-US',
                   'es_cu' : 'es-ES',
                   'es_co' : 'es-ES',
                   'es_cl' : 'es-ES',
                   'es_ar' : 'es-ES',
                   'us' : 'en-US',
                   'uk' : 'en-GB',
                   'en_ph' : 'en-US',
                   'en_ug' : 'en-US',
                   'nz' : 'en-US',
                   'en_na' : 'en-US',
                   'en_my' : 'en-US',
                   'en_ke' : 'en-US',
                   'en_ie' : 'en-UK',
                   'in' : 'en-US',
                   'ca' : 'en-CA',
                   'en_bw' : 'en-US',
                   'au' : 'en-AU',
                   'en_za' : 'en-ZA',
                   }

dico_lang = {'fr' : 'fr',
             'fr_ch' : 'fr',
             'fr_sn' : 'fr',
             'fr_ca' : 'fr',
             'fr_be' : 'fr',
             'es' : 'es',
             'es_ve' : 'es',
             'es_pe' : 'es',
             'es_mx' : 'es',
             'es_us' : 'es',
             'es_cu' : 'es',
             'es_co' : 'es',
             'es_cl' : 'es',
             'es_ar' : 'es',
             'us' : 'en',
             'uk' : 'en',
             'en_ph' : 'en',
             'en_ug' : 'en',
             'nz' : 'en',
             'en_na' : 'en',
             'en_my' : 'en',
             'en_ke' : 'en',
             'en_ie' : 'en',
             'in' : 'en',
             'ca' : 'en',
             'en_bw' : 'en',
             'au' : 'en',
             'en_za' : 'en',
             }
