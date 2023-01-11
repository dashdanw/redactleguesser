def get_wordlist():
    return [word_line.split(' ')[0] for word_line in open('enwiki-2022-08-29.txt', 'r')]