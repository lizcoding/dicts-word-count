"""Count words in file."""
def wordcount(filename):
    with open(filename) as file:
        word_count = {}
        data = file.read().split()
        for letter in data:
            word_count[letter] = word_count.get(letter, 0) + 1
        for key,value in word_count.items():
            print(f'{key}: {value}')


wordcount('test.txt')

def supercount(filename):
    with open(filename) as file:
        data = file.read().split()
        for letter in set(data):
            print(f'{letter}: {data.count(letter)}')

supercount('test.txt')