function drag() {
	doggo = document.getElementById("dog");
	leftbox = document.getElementById("leftBox");
	
	doggo.addEventListener("dragstart", startDrag, false);
	doggo.addEventListener("dragend", endDrag, false);
	
	leftbox.addEventListener("dragenter", dragEnter, false);
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) {
	var pic = '<img id = "dog" src = "https://s-media-cache-ak0.pinimg.com/originals/20/d8/53/20d8539dc87fd4e4b56fe2f60e4cdcbb.jpg">';
	e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "orange";
	leftbox.style.border = "3px solid green";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "white";
	leftbox.style.border = "3px solid purple";
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
	pic = e.target
	pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);