/*
Jason Zheng
SoftDev Pd. 2
K #05: ...and I want to Paint It Better
2020-02-06
*/

var c = document.getElementById("playground");
var ctx = c.getContext("2d");

// Clears Canvas
var clean = function() {
  ctx.clearRect(0, 0, c.width, c.height);
}

// Creates a dot at mouse location
var dot = function(){
  ctx.beginPath();
  ctx.moveTo(0,0);
  ctx.lineTo(event.clientX, event.clientY);
  ctx.stroke();
  ctx.closePath();
  ctx.beginPath();
  ctx.arc(event.clientX, event.clientY, 10, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
}

// On click run clear function
var clear = document.getElementById("clear");
clear.addEventListener("click", clean);

// On click run draw function
c.addEventListener("click", dot)
