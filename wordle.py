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

def set_yellow(c, i):
    global WORDS, TEMP_WORDS
    for word in WORDS:
        if c in word and word[i-1] != c:
            TEMP_WORDS.append(word)
    WORDS = TEMP_WORDS.copy()
    TEMP_WORDS = []

def set_chars(s, **kwargs):
    yellow_pos = []
    if 'yellow' in kwargs:
        yellow_pos = [i - 1 for i in kwargs['yellow']]
    for i in range(5):
        if i in yellow_pos:
            set_yellow(s[i], i+1)
        elif s[i] == '*':
            pass
        else:
            set_char(s[i], i+1)

def pwords():
    global WORDS
    for word in WORDS:
        print(word)

if __name__ == '__main__':
    load_file()
