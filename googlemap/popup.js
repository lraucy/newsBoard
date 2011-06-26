function addPopup(){
	$(".external_link").colorbox({width: "100%", height:"100%", iframe:true});
}
function addPopupiPad(){
	$(".external_link").click(function(){
		window.open(this.href);
		return false;
	});
}
