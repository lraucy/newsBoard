#!/usr/bin/python2
# -*-coding:Utf-8 -*

from authorization.clientlogin import ClientLogin
from sql.sqlbuilder import SQL
import ftclient
from fileimport.fileimporter import CSVImporter



if __name__ == "__main__":

    import sys, getpass

    tableid = 992564

    content = "Premier test SQL"
    location = "Paris"

    username = sys.argv[1]
    password = getpass.getpass("Enter your password: ")

    token = ClientLogin().authorize(username, password)
    ft_client = ftclient.ClientLoginFTClient(token)

    rowid = int(ft_client.query(SQL().insert(tableid, {'Content': content,
        'Location': location})).split("\n")[1])
    print rowid



# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

