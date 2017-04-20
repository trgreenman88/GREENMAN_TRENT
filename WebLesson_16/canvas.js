function text()
{
	var x = document.getElementByID("canvas");
	canvas = x.getContext("2d");
	
	
	
	canvas.font = "bold 36px Tahoma";
	canvas.textAlign = "end";
	canvas.fillText("Greenman", 300, 100);
}

window.addEventListener("load", text, false);