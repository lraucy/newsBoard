#!/usr/bin/python2
# -*-coding:Utf-8 -*

from fusiontables.authorization.clientlogin import ClientLogin
from fusiontables.sql.sqlbuilder import SQL
import fusiontables.ftclient
from fusiontables.fileimport.fileimporter import CSVImporter

import clientlogindata

from yahoo_placemaker.placemaker import placemaker

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
    p = placemaker(url)
    p.process()
    for i in range(len(p.titles)):
        if ft_client.query(SQL().select(tableid, None,"url='" +\
            str(p.main_links[i]) + "'")).count('\n')==1 and p.latitudes[i]!=0 and\
        p.longitudes[i]!=0:
            rowid = int(ft_client.query(SQL().insert(tableid, {'Title':
                str(p.titles[i]),
                'Number': str((i+1)),
                'Location': str(p.places_def[i]),
                'Date': str(p.dates[i]),
                'Latitude': str(p.latitudes[i]),
                'Longitude': str(p.longitudes[i]),
                'url': str(p.main_links[i]),
                'Picture': str(p.pictures[i]),
                'Country': str(p.countries[i]),
                'City': str(p.towns[i]),
                })).split("\n")[1])
            print rowid



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

