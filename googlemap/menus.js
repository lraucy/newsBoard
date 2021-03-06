// detection of the iPad??
//
var isiPad = navigator.userAgent.match(/iPad/i) != null;


function setLanguage(elt)
{
	var lang = $(elt).children().html();
	switch(lang)
	{
		case 'fr':
			language= 'fr';
			break;
		case 'en':
			language='en';
			break;	
		case 'es':
			language='es';
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

function menuInitialization()
{
	$("#searchInput").change(function(){
		search = $(this).val();
		mc.clearMarkers();
		setData();
		$("#news_list").html("");
	});
	$("#selectTheme select").change(function(){
		theme = $(this).val();
		mc.clearMarkers();
		setData();
		$("#news_list").html("");
	});
	
	$("#datepicker").change(function(){
		dateSelection = $(this).val();
		mc.clearMarkers();
		setData();
		$("#news_list").html("");
	});
	$("#dateend").change(function(){
		dateEnd = $(this).val();
		mc.clearMarkers();
		setData();
		$("#news_list").html("");
	});
	$(function(){
		$("#datepicker").datepicker({ dateFormat: 'mm/dd/yy'});
		$("#dateend").datepicker({ dateFormat: 'mm/dd/yy'});
	});
}

