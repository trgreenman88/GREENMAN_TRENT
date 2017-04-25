function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
}

function icon(e) {
	canvas.clearRect(0, 0, 600, 600);
	var pic = new Image();
	pic.src = "https://s-media-cache-ak0.pinimg.com/originals/16/9b/d9/169bd9727ec26ea6a7e08f8171f07a7a--munich-germany-baby-polar-bears.jpg";
	var xPos = e.clientX;
	var yPos = e.clientY;
	canvas.drawImage(pic, xPos-100, yPos-100, 200, 200);
}

window.addEventListener("load", mouse, false);
	