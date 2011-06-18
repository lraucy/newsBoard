var map;
var countryCircle;
var tableid = 1019598;
var lastWindow;

var countryList = {};

google.load('visualization', '1');

function initialize()
{
	geocoder = new google.maps.Geocoder();
	var my_map_option = {
		zoom: 2,
		center: new google.maps.LatLng(48.861846, 2.35239),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas"), my_map_option);

	setData();
	
/*	
	google.maps.event.addListener(layer, 'click', function(e) {
		$('#status_map').html(e.row['Content'].value);

		$('#news').empty();


		e.infoWindowHtml = '<div id="info_window"></div>';

		var lieu = e.row['Location'].value;

		var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT 'Content', 'Location' FROM 992564 WHERE Location='" + lieu + "'"));
		query.send(getLeftData);
	});


	google.maps.event.addListener(map, 'zoom_changed', function() {
	});*/

}

function setData() {
	var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Title, Date, Latitude, Longitude, url, Description, Picture FROM 1019598"));
	query.send(getData);

}

function getData(response) {
	numRows = response.getDataTable().getNumberOfRows();
	numCols = response.getDataTable().getNumberOfColumns();
	
	for (i = 0; i < numRows; i++) {
		var row = [];
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		placePoint(row);
	}

}

function placePoint(row) {
	if (row[2] != "" && row[3] != "")
	{
		coordinate = new google.maps.LatLng(row[2], row[3]);
		
		var marker = new google.maps.Marker({
			map: map,
			position: coordinate
		});

		google.maps.event.addListener(marker, 'click', function(event) {
			if (lastWindow) lastWindow.close();
			lastWindow = new google.maps.InfoWindow( {
				position: coordinate,
				content: '<h2><a href="' + row[4] + '">' + row[0] + '</a></h2><p>' + row[5] + '</p>'
			});
			lastWindow.open(map);
		});
	}

}
