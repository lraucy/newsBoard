from rssparser import RssParser

URL_SOURCE_ENGLISH = {

    # Etats Unis
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.uk/news?pz=1&cf=all&ned=us&hl=en&topic=ir&output=rss',

    # Royaumes Unis
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.uk/news?pz=1&cf=all&ned=uk&hl=en&topic=po&output=rss',

    # Philippines
    # A la une
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&output=rss',
    # National
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=n&output=rss',
    # Asie du sud est
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=se&output=rss',
    # International
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_ph&hl=en&topic=w&output=rss',
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

    # Ouganda
    # A la une
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&output=rss',
    # National
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=af&output=rss',
    # International
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=w&output=rss',
    # Business
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ug&hl=en&topic=m&output=rss',

    # Nouvelle Zélande
    # A la une
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&output=rss',
    # National
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=n&output=rss',
    # International
    'http://news.google.co.ug/news?pz=1&cf=all&ned=nz&hl=en&topic=w&output=rss',
    # Business
    'http://news.google.co.ug/news?pz=1&cf=all&ned=nz&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ug/news?pz=1&cf=all&ned=nz&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.ug/news?pz=1&cf=all&ned=nz&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.ug/news?pz=1&cf=all&ned=nz&hl=en&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.nz/news?pz=1&cf=all&ned=nz&hl=en&topic=po&output=rss',

    # Namibie
    # A la une
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&output=rss',
    # National
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=af&output=rss',
    # International
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=w&output=rss',
    # Business
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_na&hl=en&topic=m&output=rss',

    # Malaisie
    # A la une
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&output=rss',
    # National
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=n&output=rss',
    # Asie du sud est
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=se&output=rss',
    # International
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=w&output=rss',
    # Business
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=m&output=rss',
    # Plus populaires
    'http://news.google.com.ph/news?pz=1&cf=all&ned=en_my&hl=en&topic=po&output=rss',

    # Kenya
    # A la une
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&output=rss',
    # National
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=n&output=rss',
    # Afrique
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=af&output=rss',
    # International
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=w&output=rss',
    # Business
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=t&output=rss',
    # Sports
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.ug/news?pz=1&cf=all&ned=en_ke&hl=en&topic=m&output=rss',

    # Irelande
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_ie&hl=en&topic=m&output=rss',

    # Inde
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&topic=n&output=rss',
     # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=in&hl=en&topic=m&output=rss',

    # Canada
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=ca&hl=en&topic=m&output=rss',

    # Bostwana
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_bw&hl=en&topic=m&output=rss',

    # Australia
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&topic=w&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=au&hl=en&topic=m&output=rss',

    # Afrique du sud
    # A la une
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&output=rss',
    # International
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&topic=w&output=rss',
    # Afrique
    'http://news.google.co.za/news?pz=1&cf=all&ned=en_za&hl=en&topic=af&output=rss',
    # National
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&topic=n&output=rss',
    # Business
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&topic=b&output=rss',
    # Sciences
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&topic=t&output=rss',
    # Sport
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&topic=s&output=rss',
    # Santé
    'http://news.google.co.uk/news?pz=1&cf=all&ned=en_za&hl=en&topic=m&output=rss',

    }

URL_SOURCE_FRENCH = {

    # France
    # A la une
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&output=rss',
    # International
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&topic=w&output=rss',
    # National
    'http://news.google.ch/news/section?pz=1&cf=all&ned=fr&topic=n&ict=ln',
    # Economie
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&topic=m&output=rss',
    # Les plus lus
    'http://news.google.ch/news?pz=1&cf=all&ned=fr&hl=fr&topic=po&output=rss',

    # Suisse
    # A la une
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&output=rss',
    # International
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=w&output=rss',
    # National
    'http://news.google.ch/news/section?pz=1&cf=all&ned=fr_ch&topic=n&ict=ln',
    # Economie
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=m&output=rss',
    # Les plus lus
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ch&hl=fr&topic=po&output=rss',

    # Senegal
    # A la une
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&output=rss',
    # National
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=n&output=rss',
    # Afrique
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=af&output=rss',
    # International
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=w&output=rss',
    # Economie
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.sn/news?pz=1&cf=all&ned=fr_sn&hl=fr&topic=m&output=rss',

    # Canada
    # A la une
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&output=rss',
    # International
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=w&output=rss',
    # National
    'http://news.google.ch/news/section?pz=1&cf=all&ned=fr_ca&topic=n&ict=ln',
    # Economie
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=m&output=rss',
    # Les plus lus
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_ca&hl=fr&topic=po&output=rss',

    # Belgique
    # A la une
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&output=rss',
    # International
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=w&output=rss',
    # National
    'http://news.google.ch/news/section?pz=1&cf=all&ned=fr_be&topic=n&ict=ln',
    # Economie
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=b&output=rss',
    # Sciences
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=t&output=rss',
    # Sport
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=s&output=rss',
    # Santé
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=m&output=rss',
    # Les plus lus
    'http://news.google.ch/news?pz=1&cf=all&ned=fr_be&hl=fr&topic=po&output=rss',

    }

URL_SOURCE_SPANISH = {

    # Venezuela
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ve&hl=es&topic=n&output=rss',
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

    # Pérou
    # A la une
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&output=rss',
    # International
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=w&output=rss',
    # National
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.com.pe/news?pz=1&cf=all&ned=es_pe&hl=es&topic=po&output=rss',

    # Mexique
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_mx&hl=es&topic=po&output=rss',

    # Espagnol
     # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_us&hl=es&topic=po&output=rss',

    # Espagne
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es&hl=es&topic=po&output=rss',

    # Cuba
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cu&hl=es&topic=m&output=rss',

    # Colombie
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_co&hl=es&topic=m&output=rss',

    # Chili
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_cl&hl=es&topic=po&output=rss',

    # Argentine
    # A la une
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&output=rss'
    # International
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=w&output=rss',
    # National
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=n&output=rss',
    # Economie
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=b&output=rss',
    # Sciences
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=t&output=rss',
    # Sport
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=s&output=rss',
    # Santé
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=m&output=rss',
    # Plus populaires
    'http://news.google.co.ve/news?pz=1&cf=all&ned=es_ar&hl=es&topic=po&output=rss',

    }







for url in URL_SOURCE_ENGLISH:
    flux_rss = RssParser(url,'en-US')
    feeds = flux_rss.process()
    flux_rss.print_feeds()
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:


