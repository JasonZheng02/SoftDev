//Jason Zheng
//SoftDev1 pd2
//K12: Connect the Dots
//2020-03-31


var pic = document.getElementById("vimage");
var wipe = document.getElementById("clear");

var createDot = function(e){
  var newDot = document.createElementNS(
    "http://www.w3.org/2000/svg", "circle");
  newDot.setAttribute("fill", "blue");
  newDot.setAttribute("cx", e.offsetX);
  newDot.setAttribute("cy", e.offsetY);
  newDot.setAttribute("r", 20);

  pic.appendChild(newDot);
}

pic.addEventListener("click", createDot);
