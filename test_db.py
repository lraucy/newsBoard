#!/usr/bin/python2
from fusiontables.authorization.clientlogin import ClientLogin
from fusiontables.sql.sqlbuilder import SQL
import fusiontables.ftclient
from fusiontables.fileimport.fileimporter import CSVImporter

import clientlogindata

from yahoo_placemaker.rssparser import RssParser

import sys, getpass

URL_SOURCE_ENGLISH = {
    'http://news.google.com/news?ned=us&topic=w&output=rss',
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

URL_SOURCE_FRENCH = {
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=w&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=n&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=b&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=t&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=e&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=s&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=m&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=ir&output=rss',
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=po&output=rss',
    }



tableid = 1019598

auth = clientlogindata.ClientLoginData()

token = ClientLogin().authorize(auth.login, auth.password)
ft_client = fusiontables.ftclient.ClientLoginFTClient(token)

# Erase all datas in the google table
#ft_client.query(SQL().deleteAllRows(tableid))

for url in URL_SOURCE_FRENCH:
    flux_rss = RssParser(url,'fr-FR')
    print url
    feeds = flux_rss.process()
    for feed in feeds:
        print "\n"
        print feed.description.decode('utf-8').replace("'","\\'")

        if ft_client.query(SQL().select(tableid, None,"Title='" + feed.title.replace("'","\\'") + "'")).count('\n')==1 and (feed.place.latitude!=0 or feed.place.longitude!=0):
            rowid = int(ft_client.query(SQL().insert(tableid, {'Title':
            feed.title.replace("'","\\'"),
            'Location': str(feed.place.place).replace("'","\\'"),
            'Date': str(feed.date),
            'Number': str(feed.number),
            'Latitude': str(feed.place.latitude),
            'Longitude': str(feed.place.longitude),
            'url': str(feed.link),
            'Picture': str(feed.picture),
            'Language': str(feed.language),
            'Description': feed.description.replace("'","\\'"),
            })).split("\n")[1])
            print rowid




# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
#UnicodeDecodeError
