var map;
var countryCircle;

var countryList = {};

google.load('visualization', '1');

function initialize()
{
	var lat_init = new google.maps.LatLng(48.861846, 2.35239);
	var my_map_option = {
		zoom: 2,
		center: lat_init,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas"), my_map_option);


	
	var layer = new google.maps.FusionTablesLayer(992564);
	layer.setMap(map);

	google.maps.event.addListener(layer, 'click', function(e) {
		$('#status_map').html(e.row['Content'].value);

		$('#news').empty();


		e.infoWindowHtml = '<div id="info_window"></div>';

		var lieu = e.row['Location'].value;

		var query = new google.visualization.Query('http://www.google.com/fusiontables/gvizdata?tq=' + encodeURIComponent("SELECT 'Content', 'Location' FROM 992564 WHERE Location='" + lieu + "'"));
		query.send(getLeftData);
	});


	google.maps.event.addListener(map, 'zoom_changed', function() {
	});

}

function getLeftData(response){
	numRows = response.getDataTable().getNumberOfRows();
	numCols = response.getDataTable().getNumberOfColumns();


	for (i = 0; i < numRows; i++)
	{
		$('#news,#info_window').append('<div>');
		for (j = 0; j < numCols; j++) {
			$('#news,#info_window').append(response.getDataTable().getValue(i, j) + ', ');
		}
		$('#news,#info_window').append('</div>');
	}
}

