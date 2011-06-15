#!/usr/bin/python2
# -*-coding:Utf-8 -*

import urllib


from sgmllib import SGMLParser

class URLLister(SGMLParser):


    def reset(self):
        SGMLParser.reset(self)
        self.urls = []
        self.tags = ""
        self.process_text = False

    def start_a(self, attrs):
        href = [v for k, v in attrs if k=='href']
        rel = [v for k, v in attrs if k=='rel']
        if rel and rel == ['tag']:
            self.urls.extend(href)
            self.process_text = True
    def end_a(self):
        self.process_text = False

    def handle_data(self, data):
        if self.process_text==True:
            self.tags = self.tags + data + ' '

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

