let watchedSeries = ["black mirror", "money heist", "the big bang theory"];

let watchedSeriesLength = 3;

watchedSeries.splice(2, 1, "Friends")

let myWatchedSeries = "I watched" + " " + (watchedSeriesLength) + " " + "series" + ":" + (watchedSeries)

watchedSeries.push("Seinfeld");

watchedSeries.splice(0, 0, "Criminal minds");

watchedSeries.splice(1, 1);


console.log(watchedSeries[1][2]);


console.log(watchedSeries);
