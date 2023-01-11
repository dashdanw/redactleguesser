var submitGuess = document.getElementById('submitGuess');
var userGuess = document.getElementById('userGuess');

var page = 0;
var words = [];

async function guess(word_count=words.length, timeout=.1){
	for (var i=0; i<word_count; i++) {
		if( words.length === 0 ) {
			words = await getPage(page++);
			if (words.length == 0) {
				break;
			}
		}
		var word = words.shift();
		setTimeout(guessOnce, timeout, word)
	}
}

async function getPage(page_number){
	console.log(`http://127.0.0.1:8008/pop/?page=${page_number}`)
	return await fetch(`http://127.0.0.1:8008/pop/?page=${page_number}`)
		.then( (response) => response.json() )
		.then( (data) => {
			return data;
		});
}

async function guessOnce(word){
	userGuess.value = word;
	submitGuess.click();
}

