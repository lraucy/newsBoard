/*********************
 *
 *
 * Code from NewsBoard
 * 2011
 *
 *
 *
 * *************/


//parameters 
var initialZoom = 2;
var initialCenter = new google.maps.LatLng(48.861846, 2.35239);




var map;
var mc; //marker cluster

function initialize()
{
	var my_map_option = {
		zoom: initialZoom,
		center: initialCenter,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas"), my_map_option);
	mc = createCluster();
	styleMap(map);
	setData();
}

var newsDelay = 500;
var showTimer = null;
function createCluster()
{
	var optionsCluster = {
		zoomOnClick: true,
		maxZoom: 30,
		minimumClusterSize:1
	}
	var mc = new MarkerClusterer(map, [], optionsCluster);

	google.maps.event.addListener(mc, "clusterclick", getNewsCluster);
	google.maps.event.addListener(mc, "clustermouseover", function(cluster){
		showTimer = setTimeout(function(){
			getNewsCluster(cluster);
		}, newsDelay);
	});
	google.maps.event.addListener(mc, "clustermouseout", function(cluster){
		if (showTimer) clearTimeout(showTimer);
	});
	return mc;
}
function styleMap(map)
{
	var stylez = [ { featureType: "road", elementType: "all", stylers: [ { visibility: "off" } ] } ];
	var styledMapOptions = 
	{
		name: "newsboard"
	}
	var newsboardStyle = new google.maps.StyledMapType(stylez, styledMapOptions);
	map.mapTypes.set("newsboard", newsboardStyle);
	map.setMapTypeId("newsboard");

}

