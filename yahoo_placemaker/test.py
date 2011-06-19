#!/usr/bin/python2
# -*-coding:Utf-8 -*

from rssparser import RssParser

# URL of the source RSS flux
URL_SOURCE = {'http://news.google.com/news?ned=us&topic=w&output=rss',
        'http://news.google.com/news?ned=us&topic=h&output=rss',
        'http://news.google.com/news?ned=us&topic=b&output=rss',
        'http://news.google.com/news?ned=us&topic=t&output=rss',
        'http://news.google.com/news?ned=us&topic=m&output=rss',
        'http://news.google.com/news?ned=us&topic=s&output=rss',
        'http://news.google.com/news?ned=us&topic=e&output=rss',
        }

for url in URL_SOURCE:
    flux_rss = RssParser(url)
    feeds = flux_rss.process()
    flux_rss.print_feeds()
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

