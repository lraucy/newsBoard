#!/usr/bin/python2
# -*-coding:Utf-8 -*

from fusiontables.authorization.clientlogin import ClientLogin
from fusiontables.sql.sqlbuilder import SQL
import fusiontables.ftclient
from fusiontables.fileimport.fileimporter import CSVImporter

import clientlogindata

from yahoo_placemaker.placemaker import RssParser

URL_SOURCE = {'http://news.google.com/news?ned=us&topic=w&output=rss',
        'http://news.google.com/news?ned=us&topic=h&output=rss',
        'http://news.google.com/news?ned=us&topic=b&output=rss',
        'http://news.google.com/news?ned=us&topic=t&output=rss',
        'http://news.google.com/news?ned=us&topic=m&output=rss',
        'http://news.google.com/news?ned=us&topic=s&output=rss',
        'http://news.google.com/news?ned=us&topic=e&output=rss',
        }

import sys, getpass

tableid = 1019598

auth = clientlogindata.ClientLoginData()

token = ClientLogin().authorize(auth.login, auth.password)
ft_client = fusiontables.ftclient.ClientLoginFTClient(token)

for url in URL_SOURCE:
    flux_rss = RssParser(url)
    feeds = flux_rss.process()
    for feed in feeds:
        if ft_client.query(SQL().select(tableid, None,"url='" +\
            str(feed.link) + "'")).count('\n')==1 and feed.place.latitude==0\
        and feed.place.longitude==0:
            rowid = int(ft_client.query(SQL().insert(tableid, {'Title':
                str(feed.title),
                'Location': str(feed.place.place),
                'Date': str(feed.date),
                'Latitude': str(feed.place.latitude),
                'Longitude': str(feed.place.longitude),
                'url': str(feed.link),
                'Picture': str(feed.picture),
                'Country': str(feed.place.countrie),
                'City': str(feed.place.city),
                })).split("\n")[1])
            print rowid



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

