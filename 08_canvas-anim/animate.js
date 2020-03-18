// Jason Zheng
// SoftDev pd2
// K08: What is it saving the screen from?
// 2020-02-14
// --------------------------------------------------
//Used given code for 07_canvas-anim
//model for HTML5 canvas-based animation

//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById( "circle" );
var stopButton = document.getElementById( "stop" );
var dvdButton = document.getElementById( "dvd" );
//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to celine
ctx.fillStyle = "#00ffff";


var requestID;

//clears canvas
var clear = function(e) {
  e.preventDefault();
  ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var logo = new Image();
logo.src = "logo_dvd.jpg";
var x = Math.floor(Math.random() * c.width);
var y = Math.floor(Math.random() * c.height);
var dx = 0.5;
var dy = 0.5;

var drawDot = function() {
  window.cancelAnimationFrame( requestID );

  ctx.clearRect( 0, 0, c.width, c.height );

  if ( growing ) {
	  radius += 1;
  }
  else {
	  radius -= 1;
  }

  if ( radius == (c.width / 2) )
	  growing = false;
  else if ( radius == 0 ) {
	  growing = true;
  }

  //draw the dot
  ctx.beginPath();
  ctx.arc( c.width / 2, c.height / 2, radius, 0, 2 * Math.PI );
  ctx.stroke();
  ctx.fill();

  requestID = window.requestAnimationFrame( drawDot );
};

var showDVD = function() {
  window.cancelAnimationFrame( requestID );

  ctx.clearRect( 0, 0, c.width, c.height );

  //if logo hits the canvas
  if (x + 100 == c.width){
    dx = -0.5;
  }
  if (x == 0){
    dx = 0.5;
  }
  if (y + 100 == c.height){
    dy = -0.5;
  }
  if (y == 0){
    dy = 0.5;
  }

  x = x + dx;
  y = x + dy;

  //draw the image
  ctx.drawImage( logo , x, y, 100, 100);

  requestID = window.requestAnimationFrame( showDVD );
};

var stopIt = function() {
  window.cancelAnimationFrame( requestID );
};

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
dvdButton.addEventListener( "click", showDVD );
