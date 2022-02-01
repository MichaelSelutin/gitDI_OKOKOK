let listTasks = ["washing"];
let text = listTasks.toString();

ul = document.createElement('ul');

document.getElementById('ListOfThings').appendChild(ul);

listTasks.forEach(function (item) {
    let li = document.createElement('li');
    ul.appendChild(li);

    li.innerHTML += item;
})

document.getElementById("myButton").addEventListener("click", myFunction);

function myFunction() {
    text = document.getElementById('item').value;
    listTasks.push(text);
}

