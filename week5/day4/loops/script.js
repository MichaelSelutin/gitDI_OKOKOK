let colors = ["blue", "red", "green"]

for (let index = 0; index < colors.length; index++) {
    const element = colors[index];
 


let suffix

switch (index) {
    case 0:
        suffix = "st"
        break;
    case 1:
        suffix = "nd"
        break;
    case 2:
        suffix = "rd"
        break;               
    default:
        suffix ="th"
        break;
    }
    console.log(`my ${index+1}${suffix} favorite color is ${element}`)
}