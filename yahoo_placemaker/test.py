#!/usr/bin/python2
# -*-coding:Utf-8 -*

from placemaker import placemaker

# URL of the source RSS flux
URL_SOURCE = 'http://news.google.com/news?ned=us&topic=w&output=rss'

p = placemaker(URL_SOURCE)

p.process()
p.print_locations()
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

