//ex1

let people =["Greg", "Mary", "Devon", "James"];

people.shift(people);


let result = people.splice(2,1, "Jason");


people.push("Michael")

let index = people.indexOf("Mary");

//console.log(index)

//console.log(people.slice(1, 3));

let FooIndex = people.indexOf("Foo")
//console.log(FooIndex)

// returns -1 because index not found

let last = people[3]

//console.log(last)

//part II

//for(let i = 0; i < people.length; i++) {
  //  console.log(people[i]);
  //}

  //for(let i = 0; i < people.length; i++) {
   // console.log(people[2]);
//  }

//ex2

//let colors = ["blue", "green", "yellow", "pink", "black"]

//for(let i = 0; i < colors.length; i++) {
   //   console.log("My # " + (i+1) + " choice is " + colors[i]);
   // }

//ex3

let num = prompt("please write a number")

let i = parseInt(num)

console.log (i)
while (i < 10) {
i = prompt("please write a number"); 

if (i > 10) {break}
}


//ex4