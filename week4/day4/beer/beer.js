let bottles = prompt("How many bottles do you have?")
let them
let x
for (counter = bottles; counter >= 1; counter = counter -1) 
{
    if (counter == 1) {
        bottles = 'bottle'; 
        them = 'it';
    } else {
        bottles = 'bottles';
        them = 'them';
    }
    
    console.log(counter+" "+bottles+" of beer on the wall.");
    if (counter < 99) {
        console.log("");
        console.log(counter+" "+bottles+" of beer on the wall.");
    }
    console.log(counter+" "+bottles+" of beer.");
    console.log("Take one down.");
    console.log("Pass " +them+ " around.");
    if (counter == 1) {
        console.log("No bottles of beer on the wall.");
    }
}
