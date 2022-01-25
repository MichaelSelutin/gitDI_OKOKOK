let button = document.querySelector("button");


button.addEventListener("click", function(){

    let noun = document.getElementById("noun").value;
    let adjective = document.getElementById("adjective").value;
    let name = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;

    if (document.querySelectorAll("li").value.length == 0){
        alert("please fill out all fields")
    }
      
    document.getElementById("story").innerHTML = ("hi " + name + " great to see you. I like your new " + noun + ". Wanna go play some Football in the " + place + "! Juhuu you say full of " + adjective);
});

  
