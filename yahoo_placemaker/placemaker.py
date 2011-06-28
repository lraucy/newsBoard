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

# When using ElementTree to parse the XML returned by the API,
# each tag is prefixed by the schema URL. We need to use this
# prefix when finding tags in the document.
TAG_PREFIX = '{http://wherein.yahooapis.com/v1/schema}'
# API Key to be able tu use Yahoo PlaceMaker
API_KEY = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
# Yahoo PlaceMaker API URL
API_URL = 'http://wherein.yahooapis.com/v1/document'

import urllib
import urllib2
from xml.etree import ElementTree

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


class Placemaker(object):

    def __init__(self, lang='en-US'):
        self.lang = lang


    def find_places(self, input, documentType='text/plain',
                    outputType='xml', documentTitle='', autoDisambiguate='true',
                    focusWoeid=''):

        self.values = {'appid': API_KEY,
                       'documentType': documentType,
                       'inputLanguage': self.lang,
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
        self.places = [PlacemakerPlace(place) for place in place_details]
        return self.places


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:


