# When using ElementTree to parse the XML returned by the API,
# each tag is prefixed by the schema URL. We need to use this
# prefix when finding tags in the document.
TAG_PREFIX = '{http://where.yahooapis.com/v1/schema.rng}'
# API Key to be able tu use Yahoo PlaceMaker
API_KEY = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
# Yahoo GeoPlanet API URL
API_URL = 'http://where.yahooapis.com/v1'

import urllib
import urllib2
from xml.etree import ElementTree

class GeoplanetPlace(object):

    def __init__(self, tree):

        self.woeid = tree.find('%swoeid' % TAG_PREFIX).text
        self.placecode = tree.find('%splaceTypeName' % TAG_PREFIX).attrib.get('code')
        try:
            self.placecode = int(self.placecode)
        except ValueError:
            pass
        self.placetype = tree.find('%splaceTypeName' % TAG_PREFIX).text
        self.name = tree.find('%sname' % TAG_PREFIX).text
        self.countrytype = tree.find('%scountry' % TAG_PREFIX).attrib.get('type')
        self.countrycode = tree.find('%scountry' % TAG_PREFIX).attrib.get('code')
        self.country = tree.find('%scountry' % TAG_PREFIX).text
        self.admin1type = tree.find('%sadmin1' % TAG_PREFIX).attrib.get('type')
        self.admin1code = tree.find('%sadmin1' % TAG_PREFIX).attrib.get('code')
        self.admin1 = tree.find('%sadmin2' % TAG_PREFIX).text
        self.admin2type = tree.find('%sadmin2' % TAG_PREFIX).attrib.get('type')
        self.admin2code = tree.find('%sadmin2' % TAG_PREFIX).attrib.get('code')
        self.admin2 = tree.find('%sadmin1' % TAG_PREFIX).text
        self.admin3type = tree.find('%sadmin3' % TAG_PREFIX).attrib.get('type')
        self.admin3code = tree.find('%sadmin3' % TAG_PREFIX).attrib.get('code')
        self.admin3 = tree.find('%sadmin3' % TAG_PREFIX).text
        self.locality1 = tree.find('%slocality1' % TAG_PREFIX).text
        self.locality2 = tree.find('%slocality2' % TAG_PREFIX).text
        self.centroid = GeoplanetPoint(tree.find('%scentroid' % TAG_PREFIX))

    def __repr__(self):
        return str(self.name)

class GeoplanetPoint(object):

    def __init__(self, tree):
        self.latitude = tree.find('%slatitude' % TAG_PREFIX).text
        if self.latitude:
            self.latitude = float(self.latitude)

        self.longitude = tree.find('%slongitude' % TAG_PREFIX).text
        if self.longitude:
            self.longitude = float(self.longitude)


class Geoplanet(object):

    def __init__(self, lang='en-US'):
        self.lang = lang

    def find_places_by_woeids(self, woeid=[], format='xml', view='long'):
        self.url = API_URL + '/places.woeid(' + ','.join(str(i) for i in woeid) + ')?'
        self.values = {'appid': API_KEY,
                       'lang': self.lang,
                       'format': format,
                       'view': view,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            places = self.tree.findall('%splace' % TAG_PREFIX)
            self.places = [GeoplanetPlace(place) for place in places]
            return self.places
        except:
            return []

    def find_place_by_woeid(self, woeid=0, format='xml', view='long'):
        self.url = API_URL + '/place/' + str(woeid) + '?'
        self.values = {'appid': API_KEY,
                       'lang': self.lang,
                       'format': format,
                       'view': view,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            self.place = GeoplanetPlace(self.tree)
            return self.place
        except:
            return []

    def find_places_by_name(self, name='', format='xml', view='long', count='5'):
        self.url = API_URL + '/places.q(' + str(name)+ ');' + 'count=' + str(count) + '?'
        self.values = {'appid': API_KEY,
                       'lang': self.lang,
                       'format': format,
                       'view': view,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            places = self.tree.findall('%splace' % TAG_PREFIX)
            self.places = [GeoplanetPlace(place) for place in places]
            return self.places
        except:
            return []


    def find_parent_by_woeid(self, woeid=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/parent?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            self.parent = GeoplanetPlace(self.tree)
            return self.parent
        except:
            return []


    def find_ancestors_by_woeid(self, woeid=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/ancestors?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            ancestors = self.tree.findall('%splace' % TAG_PREFIX)
            self.ancestors = [GeoplanetPlace(ancestor) for ancestor in ancestors]
            return self.ancestors
        except:
            return []


    def find_belongtos_by_woeid(self, woeid=0, count=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/belongtos' + ';' + 'count=' + str(count) + '?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            belongtos = self.tree.findall('%splace' % TAG_PREFIX)
            self.belongtos = [GeoplanetPlace(belongto) for belongto in belongtos]
            return self.belongtos
        except:
            return []


    def find_neighbors_by_woeid(self, woeid=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/neighbors?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            neighbors = self.tree.findall('%splace' % TAG_PREFIX)
            self.neighbors = [GeoplanetPlace(neighbor) for neighbor in neighbors]
            return self.neighbors
        except:
            return []


    def find_neighbors_of_neighbors_by_woeid(self, woeid=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/neighbors.degree(2)?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            neighbors = self.tree.findall('%splace' % TAG_PREFIX)
            self.neighbors = [GeoplanetPlace(neighbor) for neighbor in neighbors]
            return self.neighbors
        except:
            return []


    def find_siblings_by_woeid(self, woeid=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/siblings?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            siblings = self.tree.findall('%splace' % TAG_PREFIX)
            self.siblings = [GeoplanetPlace(sibling) for sibling in siblings]
            return self.siblings
        except:
            return []


    def find_children_by_woeid(self, woeid=0, count=100, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/children' + ';' + 'count=' + str(count) + '?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            children = self.tree.findall('%splace' % TAG_PREFIX)
            self.children = [GeoplanetPlace(child) for child in children]
            return self.children
        except:
            return []

    def find_children_of_children_by_woeid(self, woeid=0, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/children.degree(2)?'
        self.values = {'appid': API_KEY,
                       'select': 'long',
                       'lang': self.lang,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            children = self.tree.findall('%splace' % TAG_PREFIX)
            self.children = [GeoplanetPlace(child) for child in children]
            return self.children
        except:
            return []


    def find_descendants_by_woeid(self, woeid=0, count=100, format='xml', select='long'):
        self.url = API_URL + '/place/' + str(woeid) + '/descendants' + '?'
        self.values = {'appid': API_KEY,
                       'lang': self.lang,
                       'select': select,
                       'format': format,
                       }
        try:
            self.response_xml = request_geoplanet(self.url, self.values)
            self.tree = ElementTree.fromstring(self.response_xml)
            descendants = self.tree.findall('%splace' % TAG_PREFIX)
            self.descendants = [GeoplanetPlace(descendant) for descendant in descendants]
            return self.descendants
        except:
            return []


def request_geoplanet(url, values):

    data = urllib.urlencode(values)
    req = urllib2.Request(url + data)
    response = urllib2.urlopen(req)

    response_codes = {400: 'Bad Request',
                          404: 'Not Found',
                          413: 'Request Entity Too Large',
                          415: 'Unsupported Media Type',
                          999: 'Unable to process request at this time', }

    if response.code != 200:
        raise PlacemakerApiError('Request received a response code of %d: %s' % (response.code, response_codes[response.code]))

    else:
        return response.read()





