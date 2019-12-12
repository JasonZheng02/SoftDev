var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e;
};

var removeItem = function(e) {
  //???
};
var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener( 'mouseover', function(){changeHeading(lis[i])};);
  //lis[i].addEventListener( 'mouseout' ???);
  //lis[i].addEventListener( 'click', ???);
}

button = document.getElementById('b')
button.addEventListener('click', function(e){console.log(e);});
