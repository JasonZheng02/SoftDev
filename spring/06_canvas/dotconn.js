/*
Jason Zheng
SoftDev Pd. 2
K #06: Dot Dot Dot
2020-02-11
*/

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var prevX, prevY;

// Clears Canvas
var clean = function() {
  ctx.clearRect(0, 0, c.width, c.height);
  prevX = null;
  prevY = null;
}

// Creates a dot at mouse location
var dot = function() {
  ctx.beginPath();
  ctx.arc(event.clientX, event.clientY, 10, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
}

// Creates a line segment from one dot to another
var line = function(){
  ctx.beginPath();
	ctx.moveTo(prevX,prevY);
	ctx.lineTo(event.clientX, event.clientY);
	ctx.stroke();
  ctx.closePath();
  prevX = event.clientX;
  prevY = event.clientY;
}

// On click run clear function
var clear = document.getElementById("clear");
clear.addEventListener("click", clean);

// On click run draw function
c.addEventListener("click", function(e){
  dot();
  line();
});
