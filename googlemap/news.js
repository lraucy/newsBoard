/*********************************************
 *
 *
 * NewsBoard
 * 2011
 *
 *
 * ***************************************/

//parameters
var language = "en-US"; // initial value for language
var tableid = 1019598;

var listMarkers = [];
var lastCluster;


google.load('visualization', '1');

// get the data to place on the map
function setData() {
	var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Latitude, Longitude FROM 1019598 WHERE Language='" + language + "'"));
	query.send(getData);
}

// use the data collected via SQL and place them on the map
function getData(response) {
	var numRows = response.getDataTable().getNumberOfRows();
	var numCols = response.getDataTable().getNumberOfColumns();
	
	var continents = [];
	
	listMarkers = [];
	for (i = 0; i < numRows; i++) {
		var row = [];
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		placePoint(row);
	}
	mc.addMarkers(listMarkers);
}

// place a news on the map
function placePoint(row) {
	if (row[0] != "" && row[1] != "")
	{
		var coordinate = new google.maps.LatLng(row[0], row[1]);
		
		var marker = new google.maps.Marker({
			position: coordinate
		});

		listMarkers.push(marker);
	}
}

function getNewsCluster(cluster)
{
	if(lastCluster != cluster)
	{
		lastCluster = cluster;
		if (showTimer) clearTimeout(showTimer);
		var bounds = cluster.getBounds();
		var max_lat = bounds.getNorthEast().lat();
		var max_lng = bounds.getNorthEast().lng();
		var min_lat = bounds.getSouthWest().lat();
		var min_lng = bounds.getSouthWest().lng();
		// query do not use geographic features of Fusion Tables because it needs geocoding... and we wannot geocode from python script.
		// so we use this sort of "hack"
		var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Title, Date, url, Description, Picture, Latitude, Longitude FROM 1019598 WHERE Latitude >= " + (min_lat - 0.01) + " AND Latitude <= " + (max_lat + 0.01) + " AND Longitude >= " + (min_lng - 0.01) + " AND Longitude <= " + (max_lng + 0.01) + " AND Language = '" + language + "'"));

		// we put the loading image
		$("#news_list").html('<div class="waiter"></div>');
		query.send(displayPopup);
	}
}

// function called to display the popup containing the different news on the point
function displayPopup(response) {
	var htmlContent = "";
	var numRows = response.getDataTable().getNumberOfRows();
	var numCols = response.getDataTable().getNumberOfColumns();

	for (i = 0; i < numRows; i++) {
		var row = [];
		htmlContent += '<div class="news_in_list">';
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		htmlContent += '<h3><a href="' + row[2] + '" class="external_link">' + row[0] + '</a></h3><p>' + row[3] + '</div>';
	}

	$("#news_list").html(htmlContent);
	addPopup();
	
}
