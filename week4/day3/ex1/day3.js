
    function playTheGame() {
        let randomNum = Math.floor(Math.random() * 11);

        //to see the output
        console.log(randomNum)

        let guess;
        guess = prompt("Wanna play a game?");
       
        if (guess < randomNum) {
            window.alert("Your number is smaller then the computers, guess again")
        } else if (guess > randomNum) {
            window.alert("Your number is bigger then the computers, guess again")
        } else if (guess == randomNum) {
            window.alert("WINNER")
        } else {
            window.alert("Sorry Not a number, Goodbye")
        }

    }