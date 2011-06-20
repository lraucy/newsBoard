#!/usr/bin/python2
# -*-coding:Utf-8 -*

from rssparser import RssParser

#URL of the source RSS flux
URL_SOURCE = {'http://news.google.com/news?ned=us&topic=w&output=rss',
              'http://news.google.com/news?ned=us&topic=h&output=rss',
              'http://news.google.com/news?ned=us&topic=b&output=rss',
              'http://news.google.com/news?ned=us&topic=t&output=rss',
              'http://news.google.com/news?ned=us&topic=m&output=rss',
              'http://news.google.com/news?ned=us&topic=s&output=rss',
              'http://news.google.com/news?ned=us&topic=e&output=rss',
              'http://news.google.com/news?ned=au&topic=n&output=rss',
              'http://news.google.com/news?ned=ca&topic=n&output=rss',
              'http://news.google.com/news?ned=in&topic=n&output=rss',
              'http://news.google.com/news?ned=ie&topic=n&output=rss',
              'http://news.google.com/news?ned=nz&topic=n&output=rss',
              'http://news.google.com/news?ned=en_za&topic=h&output=rss',
              'http://news.google.com/news?ned=us&topic=n&output=rss',
              'http://news.google.com/news?ned=uk&topic=n&output=rss',
        }

for url in URL_SOURCE:
    flux_rss = RssParser(url)
    feeds = flux_rss.process()
    #flux_rss.print_feeds()
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

