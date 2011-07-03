<?php 
if(preg_match("/ipad/i", $_SERVER['HTTP_USER_AGENT']))
{
	header('Content-type: text/html; charset=ISO-8859-1');
	$title = "NewsBoard: &Eacute;coutez le bruit du monde";
}
else
	$title = "NewsBoard: Écoutez le bruit du monde";
?>
<!DOCTYPE html>
<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
		<title><?php echo $title; ?></title>
		<link href="style.css" type="text/css" rel="stylesheet" media="screen">
		<link href="colorbox.css" type="text/css" rel="stylesheet" media="screen">


		<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
		<script type="text/javascript" src="https://www.google.com/jsapi?key=ABQIAAAAo_sV4ytIn5IrFe8MhmzG2RQ8RhOhhNhW6jrFcuJnspF5pmR9bBS6JJW_6pxZg3xtkcolbtpMzTcqBw"></script>
		<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js"></script>
		<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.13/jquery-ui.min.js"></script>
		<script type="text/javascript" src="jquery.colorbox-min.js"></script>

		<script type="text/javascript" src="menus.js"></script>
		<script type="text/javascript">
			$(function(){
					if (isiPad)
					{
						$("head").append(
							$(document.createElement("link")).attr({rel:"stylesheet", type:"text/css", href:"styleiPad.css", media:"screen"})
							);
						$("head").append(
							$(document.createElement("meta")).attr({name:"viewport", content:"width=768px, minimum-scale=1.0, maximum-scale=1.0"})
							);
					}
					else
					{
						$("head").append(
							$(document.createElement("link")).attr({rel:"stylesheet", type:"text/css", href:"style.css", media:"screen"})
							);
					}
				});


		</script>
		<script type="text/javascript" src="infobox_packed.js"></script>
		<script type="text/javascript" src="markerclusterer.js"></script>
		<script type="text/javascript" src="map.js"></script>
		<script type="text/javascript" src="news.js"></script>
		<script type="text/javascript" src="iPad.js"></script>
		<script type="text/javascript" src="popup.js"></script>


	</head>
	<body onload="initialize()">
<?php
if(preg_match("/iphone|android|symbian/i",
	$_SERVER['HTTP_USER_AGENT'])) {
?>
<div>Attention ! Ce site n'est pas optimisé pour votre appareil, il est possible que vous ayez des difficultés à l'utiliser.</div>
<?php
		}
?>
		<div id="container">


			<div id="content">
				<div id="left_side">
					<div id="header">
<div id="searchContainer">Search: <input type="text" name="searchInput" id="searchInput"></input></div>
<div id="language_chooser"><a href="#" onclick="dezoomMap();">Initial map</a> | <span class="lang">en</span> <a href="#" onclick="setLanguage(this);"><span class="lang">fr</span></a> <a href="#" onclick="setLanguage(this);"><span class="lang">es</span></a></div>
</div>
					<div id="map_canvas"></div>
				</div>

				<div id="right_side">
					<div id="news_list"></div>
				</div>
				<footer>
					Newsboard. First Project 2011. <a href="http://www.fondation-telecom.org">Fondation Telecom</a>
				</footer>

			</div><!-- end content -->

		</div>
	</body>
</html>
