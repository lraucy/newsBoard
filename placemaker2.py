import urllib
import feedparser
import sys

flux = feedparser.parse("http://news.google.com/news?ned=us&topic=w&output=rss")
length_flux = len(flux['entries'])

list_title = []
list_link = []
list_date = []
list_description = []

for i in range(length_flux):
    list_title.append(flux.entries[i].title)
    list_link.append(flux.entries[i].link)
    list_date.append(flux.entries[i].date)
    list_description.append(flux.entries[i].summary)

appid = '3hgLZdrV34E4RaJ_HZQPov0IGkLCJ6QWSv8PNXps8mVt4YeHXG1MXzlsQrJUqu47aNO7LXc-'
documentType = 'text/plain'

inputLanguage = 'en-US'
outputType = 'rss'
characterLimit = '50000'
autoDisambiguate = True

url = 'http://wherein.yahooapis.com/v1/document'
response = []

for i in range(length_flux):
    values = { 'appid': appid,
               'documentType': documentType,
               'documentContent': list_description[i],
               'inputLanguage': inputLanguage,
               'outputType' : outputType,
               'characterLimit' : characterLimit,
               'autoDisambiguate' : autoDisambiguate, }
    try:
        data = urllib.urlencode(values)
    except UnicodeEncodeError:
        continue
    response.append(urllib.urlopen(url, data))

for i in range(len(response)):
     flux = feedparser.parse(response[i])
     print flux.entries[0].title
#    print flux.entries[0].link
#    print flux.entries[0].description
#    print response[i].read()















