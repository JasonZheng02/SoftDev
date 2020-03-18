/*
Jason Zheng
SoftDev Pd. 2
K #05: ...and I want to Paint It Better
2020-02-06
*/

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
var shape = "Box";

// Clears Canvas
var clear = function() {
  ctx.clearRect(0, 0, c.width, c.height);
}

// Creates a box at mouse location
var box = function() {
  ctx.fillRect(event.clientX, event.clientY, 50, 100);
}

// Creates a dot at mouse location
var dot = function(){
  ctx.beginPath();
  ctx.arc(event.clientX, event.clientY, 10, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
}

// Switches desired shape
var change = function(){
  if (shape == "Box"){
    shape = "Dot";
    toggle.innerHTML = "Dot";
  }
  else{
    shape = "Box";
    toggle.innerHTML = "Box";
  }
}

// Creates desired shape
var draw = function(){
  if (shape == "Box"){
    box();
  }
  else {
    dot();
  }
}

// On click run clear function
var clean = document.getElementById("clean");
clean.addEventListener("click", clear);

// On click run change function
var toggle = document.getElementById("toggle");
toggle.addEventListener("click", change);

// On click run draw function
c.addEventListener("click", draw)

/*
e.preventDefault() tells the user agent that
if the event does not get explicitly handled,
its default action should not be taken as it
normally would be.

ctx.beginPath() starts a new path by emptying
the list of sub-paths.

e.offsetX provides the offset in the X coordinate
of the mouse pointer between that event and the
padding edge of the target node.

e.offsetY provides the offset in the Y coordinate
of the mouse pointer between that event and the
padding edge of the target node.
*/
