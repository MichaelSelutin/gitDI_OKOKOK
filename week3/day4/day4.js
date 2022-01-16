// ex1

let x = 9;
let y = 7;

if (x > y) {
console.log("x is the biggest number");
} 

else {
console.log("x is the smaller number");
}


// ex2

let newDog = "Chihuahua"

let length = newDog.length

console.log(length)

//ex3

let number = prompt("Please write a number")

if (number%2 == 0) {
    console.log(number + " is an even number")
} else {
    console.log(number + " is an odd number")
}


//ex4

let users = prompt("How many people are online?")


if (users == 1) {
   let user1 = prompt("whats your name?")
    console.log(user1 + " is online")

} 

else if (users == 2) {
        let user2 = prompt("what are your names?")
        console.log(user2 + " are online")
}

else if (users => 3) {
    let visitor1 = prompt("what is your name?")
    let visitor2 = prompt("what is your name?")
    console.log(visitor1 + visitor2 + "users"-2 + "are online")

}