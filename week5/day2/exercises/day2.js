//ex1

console.log(document.querySelector("h1"))


let parentElem = document.getElementsByTagName("article");
console.log(parentElem)

let childElem = document.getElementsByTagName("p")[[3]];
console.log(childElem)

//let removed = parentElem.remove(childElem);


let head2 = document.querySelector("h2")

console.log(head2)

head2.addEventListener("click", function(){
    head2.style.background = "green"
});

let head3 = document.querySelector("h3")

head3.addEventListener("click", function(){
    head3.style.display = "none";
})

let button = document.querySelector("button")
let Ps = document.getElementsByTagName("p")

button.addEventListener("click", function(){
  //  Ps.style.fontWeight = "900"
});


//ex2

let table = document.getElementsByTagName("form");

documents.form;

let elem = form.elements[0]

console.log(elem)
