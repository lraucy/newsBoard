#!/usr/bin/python2
# -*- coding: utf-8 -*-

from fusiontables.authorization.clientlogin import ClientLogin
from fusiontables.sql.sqlbuilder import SQL
import fusiontables.ftclient
from fusiontables.fileimport.fileimporter import CSVImporter

import clientlogindata

from yahoo_placemaker.rssparser import RssParser

import sys, getpass



URL_SOURCE = [

    #ANGLAIS

    # Etats Unis
    # Business
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=s&output=rss',
    # Sante
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss',
    # Plus populaires
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=ir&output=rss',
    # International
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=w&output=rss',
    # National
    'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&topic=n&output=rss',

    # Royaumes Unis
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&output=rss',
    # Plus populaires
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=po&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=n&output=rss',

    # Philippines
    # A la une
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&output=rss',
    # Business
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=m&output=rss',
    # Plus populaires
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=po&output=rss',
    # Asie du sud est
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=se&output=rss',
    # International
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=w&output=rss',
    # National
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=n&output=rss',

    # Ouganda
    # Business
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&output=rss',
    # National
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=af&output=rss',
    # International
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=w&output=rss',

    # Nouvelle Zélande
    # Business
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&output=rss',
    # Plus populaires
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=po&output=rss',
    # National
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=n&output=rss',
    # International
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=w&output=rss',

    # Namibie
    # Business
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&output=rss',
    # National
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=af&output=rss',
    # International
    'http://news.google.com.na/news?pz=1&cf=all&ned=en_na&hl=en&topic=w&output=rss',

    # Malaisie
    # Business
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&output=rss',
    # Plus populaires
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=po&output=rss',
    # National
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=n&output=rss',
    # Asie du sud est
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=se&output=rss',
    # International
    'http://news.google.com.my/news?pz=1&cf=all&ned=en_my&hl=en&topic=w&output=rss',


    # Kenya
    # Business
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&output=rss',
    # National
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=af&output=rss',
    # International
    'http://news.google.co.ke/news?pz=1&cf=all&ned=en_ke&hl=en&topic=w&output=rss',

    # Irelande
    # Business
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&output=rss',
    # National
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&topic=n&output=rss',
    # International
    'http://news.google.ie/news?pz=1&cf=all&ned=en_ie&hl=en&topic=w&output=rss',

    # Inde
    # Business
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&output=rss',
    # National
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&topic=n&output=rss',
    # International
    'http://news.google.co.in/news?pz=1&cf=all&ned=in&hl=en&topic=w&output=rss',

    # Canada
    # Business
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&output=rss',
    # National
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&topic=n&output=rss',
    # International
    'http://news.google.ca/news?pz=1&cf=all&ned=ca&hl=en&topic=w&output=rss',

    # Bostwana
    # Business
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&output=rss',
    # National
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&topic=n&output=rss',
    # International
    'http://news.google.co.bw/news?pz=1&cf=all&ned=en_bw&hl=en&topic=w&output=rss',

    # Australia
    # Business
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&output=rss',
    # National
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&topic=n&output=rss',
    # International
    'http://news.google.com.au/news?pz=1&cf=all&ned=au&hl=en&topic=w&output=rss',

    # Afrique du sud
    # Business
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=m&output=rss',
    # A la une
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&output=rss',
    # National
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=af&output=rss',
    # International
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=w&output=rss',



    # FRANCAIS

    # France
    # Economie
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=m&output=rss',
    # A la une
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&output=rss',
    # Les plus lus
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=po&output=rss',
    # National
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=n&output=rss',
    # International
    'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&topic=w&output=rss',

    # Suisse
    # Economie
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=m&output=rss',
    # A la une
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&output=rss',
    # Les plus lus
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=po&output=rss',
    # National
    'http://news.google.fr/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=n&output=rss',
    # International
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=w&output=rss',

    # Senegal
    # Economie
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=m&output=rss',
    # A la une
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&output=rss',
    # Afrique
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=af&output=rss',
    # National
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=n&output=rss',
    # International
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=w&output=rss',

    # Canada
    # Economie
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=m&output=rss',
    # A la une
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&output=rss',
    # Les plus lus
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=po&output=rss',
    # National
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=n&output=rss',
    # International
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=w&output=rss',

    # Belgique
    # Economie
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=m&output=rss',
    # A la une
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&output=rss',
    # Les plus lus
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=po&output=rss',
    # National
    'http://news.google.ca/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=n&output=rss',
    # International
    'http://news.google.be/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=w&output=rss',



    # ESPAGNOL

    # Venezuela
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=po&output=rss',
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&output=rss'
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=n&output=rss',
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=w&output=rss',

    # Pérou
    # Economie
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&output=rss',
    # Plus populaires
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=po&output=rss',
    # National
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=n&output=rss',
    # International
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=w&output=rss',

    # Mexique
    # Economie
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&output=rss'
    # Plus populaires
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=po&output=rss',
    # National
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=n&output=rss',
    # International
    'http://news.google.com.mx/news?pz=1&cf=all&ned=es_mx&hl=es&topic=w&output=rss',

    # Espagnol
    # Economie
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&output=rss'
    # Plus populaires
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=po&output=rss',
    # National
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=n&output=rss',
    # International
    'http://news.google.com/news?pz=1&cf=all&ned=es_us&hl=es&topic=w&output=rss',

    # Espagne
    # Economie
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&output=rss'
    # Plus populaires
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=po&output=rss',
    # National
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=n&output=rss',
    # International
    'http://news.google.es/news?pz=1&cf=all&ned=es&hl=es&topic=w&output=rss',

    # Cuba
    # Economie
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&output=rss'
    # National
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&topic=n&output=rss',
    # International
    'http://news.google.com.cu/news?pz=1&cf=all&ned=es_cu&hl=es&topic=w&output=rss',

    # Colombie
    # Economie
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&output=rss'
    # National
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&topic=n&output=rss',
    # International
    'http://news.google.com.co/news?pz=1&cf=all&ned=es_co&hl=es&topic=w&output=rss',

    # Chili
    # Economie
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&output=rss'
    # Plus populaires
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=po&output=rss',
    # National
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=n&output=rss',
    # International
    'http://news.google.cl/news?pz=1&cf=all&ned=es_cl&hl=es&topic=w&output=rss',

    # Argentine
    # Economie
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=m&output=rss',
    # A la une
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&output=rss'
    # Plus populaires
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=po&output=rss',
    # National
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=n&output=rss',
    # International
    'http://news.google.com.ar/news?pz=1&cf=all&ned=es_ar&hl=es&topic=w&output=rss',

    ]

tableid = 1019598

auth = clientlogindata.ClientLoginData()

token = ClientLogin().authorize(auth.login, auth.password)
ft_client = fusiontables.ftclient.ClientLoginFTClient(token)

# Erase all datas in the google table
#ft_client.query(SQL().deleteAllRows(tableid))

for url in URL_SOURCE:
    flux_rss = RssParser(url)
    print url
    feeds = flux_rss.process()
    for feed in feeds:
        print "\n"
        try :
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
            'Language': str(feed.lang),
            'Topic': str(feed.topic),
            'Source' : str(feed.source),
            'Description': feed.description.replace("'","\\'"),
            })).split("\n")[1])
            print rowid
        except :
            pass

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
#UnicodeDecodeError
