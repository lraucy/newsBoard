
var lastOrientation;

function iPadInitialization(){
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

function contentPopupiPad(response, numRows, numCols)
{
	var htmlContent = "";
	for (i = 0; i < numRows; i++) {
		var row = [];
		if (window.orientation == 0 || window.orientation == 180) htmlContent += '<td>'
			htmlContent += '<div class="news_in_list">';
		for (j = 0; j < numCols; j++) {
			row.push(response.getDataTable().getValue(i, j));
		}
		//date
		var date = new Date(Date.parse(row[1]));
		if (language == "en")
			var dateFormat = (date.getMonth()+1) + "/" + date.getDate() + "/" + date.getFullYear();
		else
			var dateFormat = date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear();
		htmlContent += '<h3><a href="' + row[2] + '" class="external_link">' + row[0] + '</a></h3><h4><span class="source">' + row[6] + '</span> - <span class="theme">' + row[7] + '</span> - <span class="newsDate">' + dateFormat  + '</span> - <span class="newsLocation">' + row[8] + '</span></h4><p>' + row[3] + '</p></div>';
		if (window.orientation == 0 || window.orientation == 180) htmlContent += '</td>'
	}
	return htmlContent;

}
