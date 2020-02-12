/*
Jason Zheng
SoftDev Pd. 2
K #07: They lock us in the tower whenever we get caught
2020-02-13
*/

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var radius = 10;
var isIncreasing = true;
var id;

// Creates a dot at mouse location
var dot = function() {
  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
  if (radius == c.width / 2 || radius == c.height / 2) {
    isIncreasing = false;
  }
  if (radius == 10){
    isIncreasing = true;
  }
  if (isIncreasing){
    radius = radius + 0.5;
  }
  else {
    radius = radius - 0.5;
  }
  window.requestAnimationFrame(dot);
}

var start = document.getElementById("animation");
start.addEventListener("click", dot);

c.addEventListener("click", dot);
