var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e;
};

var removeItem = function(e) {
  e.remove()
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener( 'mouseover', function(){changeHeading(this.innerHTML)});
  lis[i].addEventListener( 'mouseout', function(){changeHeading("Hello World!")});
  lis[i].addEventListener( 'click', function(){removeItem(this)});
}

var addItem = function() {
  var list = document.getElementById("thelist");
  var ele = document.createElement("li");
  ele.innerHTML = "WORD";
  list.append(ele);
  ele.addEventListener('click', function(e){removeItem(this), console.log(e);});
  ele.addEventListener('mouseover', function(){changeHeading(this.innerHTML)});
  ele.addEventListener('mouseout', function(){changeHeading("Hello World!")});
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);
