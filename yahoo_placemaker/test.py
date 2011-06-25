#!/usr/bin/python2
# -*-coding:Utf-8 -*

from rssparser import RssParser

start = [67.6789,  33.9305]
end = [2.03453, 47.0822]


#URL of the source RSS flux
URL_SOURCE = {'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=w&output=rss',
              'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=n&output=rss',
              'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&output=rss',
              'http://news.google.fr/news/section?pz=1&cf=all&ned=fr&topic=b&ict=ln',
              'http://news.google.fr/news/section?pz=1&cf=all&ned=fr&topic=t&ict=ln',
              'http://news.google.fr/news/section?pz=1&cf=all&ned=fr&topic=s&ict=ln',
              'http://news.google.fr/news/section?pz=1&cf=all&ned=fr&topic=m&ict=ln',
              'http://news.google.fr/news/section?pz=1&cf=all&ned=fr&topic=ir&ict=ln',
              'http://news.google.fr/news/section?pz=1&cf=all&ned=fr&topic=po&ict=ln',
              # 'http://news.google.com/news?ned=us&topic=h&output=rss',
              # 'http://news.google.com/news?ned=us&topic=b&output=rss',
              # 'http://news.google.com/news?ned=us&topic=t&output=rss',
              # 'http://news.google.com/news?ned=us&topic=m&output=rss',
              # 'http://news.google.com/news?ned=us&topic=s&output=rss',
              # 'http://news.google.com/news?ned=us&topic=e&output=rss',
              # 'http://news.google.com/news?ned=au&topic=n&output=rss',
              # 'http://news.google.com/news?ned=ca&topic=n&output=rss',
              # 'http://news.google.com/news?ned=in&topic=n&output=rss',
              # 'http://news.google.com/news?ned=ie&topic=n&output=rss',
              # 'http://news.google.com/news?ned=nz&topic=n&output=rss',
              # 'http://news.google.com/news?ned=en_za&topic=h&output=rss',
              # 'http://news.google.com/news?ned=us&topic=n&output=rss',
              # 'http://news.google.com/news?ned=uk&topic=n&output=rss',
        }

# for url in URL_SOURCE:
#     flux_rss = RssParser(url,'fr-FR')
#     feeds = flux_rss.process()
#     #flux_rss.print_feeds()
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:


