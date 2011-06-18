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
	var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Latitude, Longitude FROM 1019598"));
	query.send(getData);

}

function getData(response) {
	var numRows = response.getDataTable().getNumberOfRows();
	var numCols = response.getDataTable().getNumberOfColumns();
	
	for (i = 0; i < numRows; i++) {
		var row = [];
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		placePoint(row);
	}
}

function placePoint(row) {
	if (row[0] != "" && row[1] != "")
	{
		var coordinate = new google.maps.LatLng(row[0], row[1]);
		
		var marker = new google.maps.Marker({
			map: map,
			position: coordinate
		});

		google.maps.event.addListener(marker, 'click', function(event) {
			if (lastWindow) lastWindow.close();
			var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Title, Date, url, Description, Picture, Latitude, Longitude FROM 1019598 WHERE Latitude='" + row[0] + "' AND Longitude='" + row[1] + "'"));
			query.send(displayPopup);
				});
	}
}

function displayPopup(response) {
	var htmlContent = "";
	var numRows = response.getDataTable().getNumberOfRows();
	var numCols = response.getDataTable().getNumberOfColumns();

	coordinate = new google.maps.LatLng(response.getDataTable().getValue(0, 5), response.getDataTable().getValue(0,6));
	for (i = 0; i < numRows; i++) {
		var row = [];
		htmlContent += '<div class="news_in_list">';
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		htmlContent += '<h3><a href="' + row[2] + '">' + row[0] + '</a></h3><p>' + row[3] + '</div>';
	}
	lastWindow = new google.maps.InfoWindow( {
		position: coordinate,
		content: htmlContent
	});
	lastWindow.open(map);
}
