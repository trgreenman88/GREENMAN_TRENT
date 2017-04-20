function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	var g = canvas.createLinearGradient(0, 0, 200, 200);
	g.addColorStop(0, "purple");
	g.addColorStop(1, "yellow");
	canvas.strokeStyle = "black";
	canvas.fillStyle = g;
	canvas.beginPath();
	canvas.moveTo(0, 100);/*starting middle and far left*/
	canvas.lineTo(50, 75);
	canvas.lineTo(25, 25);
	canvas.lineTo(75, 50);
	canvas.lineTo(100, 0);
	canvas.lineTo(125, 50);
	canvas.lineTo(175, 25);
	canvas.lineTo(150, 75);
	canvas.lineTo(200, 100);
	canvas.lineTo(150, 125);
	canvas.lineTo(175, 175);
	canvas.lineTo(125, 150);
	canvas.lineTo(100, 200);
	canvas.lineTo(75, 150);
	canvas.lineTo(25, 175);
	canvas.lineTo(50, 125);
	canvas.closePath();
	canvas.stroke();
	canvas.fill() = g;
	
}

window.addEventListener("load", shapes, false);