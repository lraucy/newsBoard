var map;
var countryCircle;
var tableid = 1019598;
var lastWindow;
var boxText;
var listMarkers = [];

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
	var mc = new MarkerClusterer(map);

	setData();
	
	boxText = document.createElement("div");
	boxText.style.cssText = "border: 1px solid black; margin-top: 8px; background: #f5f5f5; padding: 5px;";
	google.maps.event.addListener(map, 'zoom_changed', function(event){if(lastWindow) lastWindow.close();});
}


// get the data to place on the map
function setData() {
	var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Latitude, Longitude FROM 1019598"));
	query.send(getData);

}

// use the data collected via SQL and place them on the map
function getData(response) {
	var numRows = response.getDataTable().getNumberOfRows();
	var numCols = response.getDataTable().getNumberOfColumns();
	
	var continents = [];
	
	for (i = 0; i < numRows; i++) {
		var row = [];
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		placePoint(row);
	}
	var optionsCluster = {
		zoomOnClick: false,
		maxZoom: 8,
		minimumClusterSize:1
	}
	var MarkerCluster = new MarkerClusterer(map, listMarkers, optionsCluster);
	google.maps.event.addListener(MarkerCluster, "clusterclick", click_cluster);
}


function click_cluster(cluster)
{
	if (lastWindow) lastWindow.close();
	var bounds = cluster.getBounds();
	var max_lat = bounds.getNorthEast().lat();
	var max_lng = bounds.getNorthEast().lng();
	var min_lat = bounds.getSouthWest().lat();
	var min_lng = bounds.getSouthWest().lng();
	// query do not use geographic features of Fusion Tables because it needs geocoding... and we wannot geocode from python script.
	// so we use this sort of "hack"
	var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Title, Date, url, Description, Picture, Latitude, Longitude FROM 1019598 WHERE Latitude >= " + (min_lat - 0.01) + " AND Latitude <= " + (max_lat + 0.01) + " AND Longitude >= " + (min_lng - 0.01) + " AND Longitude <= " + (max_lng + 0.01)));
	query.send(displayPopup);
}


// place a news on the map
function placePoint(row) {
	if (row[0] != "" && row[1] != "")
	{
		var coordinate = new google.maps.LatLng(row[0], row[1]);
		
		var marker = new google.maps.Marker({
			position: coordinate
		});

		// event when click, search all the news on this point
		google.maps.event.addListener(marker, 'click', function(event) {
			if (lastWindow) lastWindow.close();
			var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Title, Date, url, Description, Picture, Latitude, Longitude FROM 1019598 WHERE Latitude='" + row[0] + "' AND Longitude='" + row[1] + "'"));
			query.send(displayPopup);
				});
		listMarkers.push(marker);
	}
}

// function called to display the popup containing the different news on the point
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
		htmlContent += '<h3><a href="' + row[2] + '" class="external_link">' + row[0] + '</a></h3><p>' + row[3] + '</div>';
	}
	boxText.innerHTML = htmlContent;
	var myOptions = {
		content: boxText,
		disableAutoPan: false,
		maxWidth: 0,
		pixelOffset: new google.maps.Size(0, -140),
		zIndex: null,
		boxStyle: {
			opacity: 0.90,
			width: "280px",
			height: "100px"
		},
		closeBoxMargin: "10px 2px 2px 2px",
		closeBoxURL: "http://www.google.com/intl/en_us/mapfiles/close.gif",
		infoBoxClearance: new google.maps.Size(1, 1),
		isHidden:false,
		pane: "floatPane",
		enableEventPropagation: true,
		position: coordinate
	};

	lastWindow = new InfoBox(myOptions);
	google.maps.event.addListener(lastWindow, 'domready', addPopup);
	lastWindow.open(map);
}
