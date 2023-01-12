# RedactleGuesser
a script that parses a list of most common words in wordpress and allows you to rapidly enter solutions

## Usage
1. run the local server with python via `python server.py`, this will load a list of words by their frequency of occurence in all of wikipedia
2. take the code from api.js and paste it into your developer console
3. in developer console, automatically take a certain number of guesses by executing `guess(<number_of_guesses>)`, this will keep a queue of words and consume from it every time you execute the function

(it's best to guess in groups of less than 500, ie. `guess(500)`)
