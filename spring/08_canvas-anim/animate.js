// Jason Zheng
// SoftDev pd2
// K08: What is it saving the screen from?
// 2020-02-14
// --------------------------------------------------

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

var clear = function(e) {
  e.preventDefault();
  ctx.clearRect(0, 0, 500, 500);
};


var radius = 0;
var growing = true;
var x = 10;
var y = 10;
var logo = new Image();
logo.src = "logo_dvd.jpg";

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


  ctx.drawImage( logo , x, y);
  x = x + .1;
  y = x + .1;
  requestID = window.requestAnimationFrame( showDVD );
};

var stopIt = function() {
  window.cancelAnimationFrame( requestID );
};

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
dvdButton.addEventListener( "click", showDVD );
