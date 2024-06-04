WORDS = []
TEMP_WORDS = []

def load_file(f = 'words.txt'):
    global WORDS
    with open(f) as infile:
        for word in infile:
            WORDS.append(word.strip())

def remove_char(c):
    global WORDS, TEMP_WORDS
    for word in WORDS:
        if word.count(c) == 0:
            TEMP_WORDS.append(word)
    WORDS = TEMP_WORDS.copy()
    TEMP_WORDS = []

def set_char(c, i):
    global WORDS, TEMP_WORDS
    for word in WORDS:
        if word[i-1] == c:
            TEMP_WORDS.append(word)
    WORDS = TEMP_WORDS.copy()
    TEMP_WORDS = []

def pwords():
    global WORDS
    for word in WORDS:
        print(word)

if __name__ == '__main__':
    load_file()
