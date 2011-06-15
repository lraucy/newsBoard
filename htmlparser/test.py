#!/usr/bin/python2
# -*-coding:Utf-8 -*
import urllib, urllister
usock = urllib.urlopen("http://www.lefigaro.fr/sante/2011/06/15/01004-20110615ARTFIG00354-vers-une-vache-capable-de-produire-du-lait-maternel.php")
parser = urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls: print url
print parser.tags

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

