function addPopup(){
	$(".external_link").click(function(){
		window.open(this.href);
		return false;
	});
}
