function myMove() {
    var elem = document.getElementById("animate");
    var width = 0;
    let id = setInterval(function() {
      if (width == 100) {
        clearInterval(id);
      
      }
      else {
        width++;
        elem.style.width = width + '%';
           }
    }, 5);
  }



  