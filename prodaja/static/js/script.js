var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 9000);    
}

$( function() {
  var availableTags=[
    "Limun",
    "Narandža",
    "Kivi",
    "Jabuka",
    "Jagoda",
    "Luk",
    "Krastavac",
    "Paradajz",
    "Paprika",
  ];
  
  
  $( "#tags" ).autocomplete({
    source: availableTags
  });
} );

