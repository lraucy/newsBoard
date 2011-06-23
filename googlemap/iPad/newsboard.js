var map;
var countryCircle;
var tableid = 1019598;
var boxText;
var listMarkers = [];

var countryList = {};

var lastCluster;

var lastOrientation;

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

	lastOrientation = orientation;
	window.onorientationchange = function () {
		if (lastOrientation - orientation == 90 || lastOrientation - orientation == -90 || lastOrientation - orientation == 270 || lastOrientation - orientation == -270)
		{
			if (orientation == 90 || orientation == -90)
			{
				$("#news_list").unwrap();
				$("#news_list").unwrap();
				$("#news_list").unwrap();
				$(".news_in_list").unwrap();
			}
			else if (orientation == 0 || orientation == 180)
			{
				$("#news_list").wrap("<table><tr></tr></table>");
				$(".news_in_list").wrap("<td />");
			}
		}
		lastOrientation = orientation;
	}

	if(orientation == 180 || orientation == 0)
	{
		$("#news_list").wrap("<table><tr></tr></table>");
	}
	touchScroll("news_list");
}


// get the data to place on the map
function setData() {
	var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Latitude, Longitude FROM 1019598"));
	query.send(getData);

}

var newsDelay = 500;
var showTimer = null;
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
		zoomOnClick: true,
		maxZoom: 30,
		minimumClusterSize:1
	}
	var MarkerCluster = new MarkerClusterer(map, listMarkers, optionsCluster);
	google.maps.event.addListener(MarkerCluster, "clusterclick", getNewsCluster);
	google.maps.event.addListener(MarkerCluster, "clustermouseover", function(cluster){
		showTimer = setTimeout(function(){
			getNewsCluster(cluster);
		}, newsDelay);
	});
	google.maps.event.addListener(MarkerCluster, "clustermouseout", function(cluster){
		if (showTimer) clearTimeout(showTimer);
	});
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
		var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT Title, Date, url, Description, Picture, Latitude, Longitude FROM 1019598 WHERE Latitude >= " + (min_lat - 0.01) + " AND Latitude <= " + (max_lat + 0.01) + " AND Longitude >= " + (min_lng - 0.01) + " AND Longitude <= " + (max_lng + 0.01)));
		query.send(displayPopup);
	}
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

	for (i = 0; i < numRows; i++) {
		var row = [];
		if (window.orientation == 0 || window.orientation == 180) htmlContent += '<td>'
			htmlContent += '<div class="news_in_list">';
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		htmlContent += '<h3><a href="' + row[2] + '" class="external_link">' + row[0] + '</a></h3><p>' + row[3] + '</div>';
		if (window.orientation == 0 || window.orientation == 180) htmlContent += '</td>'
	}



	$("#news_list").fadeOut(100, function(){
		$(this).html(htmlContent).fadeIn(300);
		addPopup();
	});

}


function touchScroll(id){
	var el=document.getElementById(id);
	var scrollStartPosY=0;
	var scrollStartPosX=0;

	document.getElementById(id).addEventListener("touchstart", function(event) {
		scrollStartPosY=this.scrollTop+event.touches[0].pageY;
		scrollStartPosX=this.scrollLeft+event.touches[0].pageX;
	},false);

	document.getElementById(id).addEventListener("touchmove", function(event) {
		event.preventDefault();	
		this.scrollTop=scrollStartPosY-event.touches[0].pageY;
		this.scrollLeft=scrollStartPosX-event.touches[0].pageX;
	},false);
}
