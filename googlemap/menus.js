function setLanguage(elt)
{
	var lang = $(elt).children().html();
	switch(lang)
	{
		case 'fr':
			language= 'fr-FR';
			break;
		case 'en':
			language='en-US';
			break;	
	}
	mc.clearMarkers();
	setData();
	$("#news_list").html("");

	$("#language_chooser a .lang").unwrap();
	$("#language_chooser .lang").each(function(){
		if($(this).html() != lang)
		{
			$(this).wrap('<a href="#" onclick="setLanguage(this)"></a>');
		}
	});

	return false;
}

function dezoomMap()
{
	map.setZoom(initialZoom);
	map.setCenter(initialCenter);
	return false;
}

