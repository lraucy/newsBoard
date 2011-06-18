#!/usr/bin/python2
# -*-coding:Utf-8 -*

from placemaker import RssParser

# URL of the source RSS flux
URL_SOURCE = 'http://news.google.com/news?ned=us&topic=s&output=rss'

flux_rss = RssParser(URL_SOURCE)
feeds = flux_rss.process()
flux_rss.print_feeds()
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

