#!/usr/bin/python2
# -*-coding:Utf-8 -*

from fusiontables.authorization.clientlogin import ClientLogin
from fusiontables.sql.sqlbuilder import SQL
import fusiontables.ftclient
from fusiontables.fileimport.fileimporter import CSVImporter

from yahoo_placemaker.placemaker import placemaker

URL_SOURCE = 'http://news.google.com/news?ned=us&topic=w&output=rss'

import sys, getpass

tableid = 1011402

username = sys.argv[1]
password = getpass.getpass("Enter your password: ")

token = ClientLogin().authorize(username, password)
ft_client = fusiontables.ftclient.ClientLoginFTClient(token)

p = placemaker(URL_SOURCE)

p.process()
for i in range(len(p.titles)):
    rowid = int(ft_client.query(SQL().insert(tableid, {'Title':
        str(p.titles[i]),
        'Number': str((i+1)),
        'Location': str(p.places_def[i]),
        'Date': str(p.dates[i]),
        'Latitude': str(p.latitudes[i]),
        'Longitude': str(p.longitudes[i])
        })).split("\n")[1])
    print rowid



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

