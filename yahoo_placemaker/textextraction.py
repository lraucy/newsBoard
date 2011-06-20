# When using ElementTree to parse the XML returned by the API,
# each tag is prefixed by the schema URL. We need to use this
# prefix when finding tags in the document.
TAG_PREFIX = '{urn:yahoo:cate}'
# API Key to be able tu use Yahoo PlaceMaker
API_KEY = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
# Yahoo GeoPlanet API URL
API_URL = 'http://search.yahooapis.com/ContentAnalysisService/V1/termExtraction'

import urllib
import urllib2
from xml.etree import ElementTree

class TermExtractor(object):

    def extraction(self, context='', output ='xml',):
        self.values = {'context': context,
                       'appid': API_KEY,
                       'output': output,
                       }

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
        results = self.tree.findall('%sResult' % TAG_PREFIX)
        self.results= [result.text for result in results]

        return self.results



