WORDS = []
TEMP_WORDS = []
FREQ_DICT = {} #{c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
WORD_SCORES = {}

def load_file(f = 'words.txt'):
    global WORDS
    with open(f) as infile:
        for word in infile:
            WORDS.append(word.strip())
    make_word_scores()

def remove_char(c):
    global WORDS, TEMP_WORDS, WORD_SCORES
    for word in WORDS:
        WORD_SCORES[word] = 0
        if word.count(c) == 0:
            TEMP_WORDS.append(word)
    WORDS = TEMP_WORDS.copy()
    TEMP_WORDS = []
    make_word_scores()

def set_char(c, i):
    global WORDS, TEMP_WORDS, WORD_SCORES
    for word in WORDS:
        WORD_SCORES[word] = 0
        if word[i-1] == c:
            TEMP_WORDS.append(word)
    WORDS = TEMP_WORDS.copy()
    TEMP_WORDS = []
    make_word_scores()

def set_yellow(c, i):
    global WORDS, TEMP_WORDS
    for word in WORDS:
        if c in word and word[i-1] != c:
            TEMP_WORDS.append(word)
    WORDS = TEMP_WORDS.copy()
    TEMP_WORDS = []
    make_word_scores()

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
    make_word_scores()

def make_freq_dict():
    global FREQ_DICT
    global WORDS
    for c in 'abcdefghijklmnopqrstuvwxyz':
        FREQ_DICT[c] = 0
    for word in WORDS:
        for c in word:
            FREQ_DICT[c] += 1

def make_word_scores():
    global WORD_SCORES
    global FREQ_DICT
    global WORDS
    make_freq_dict()
    for word in WORDS:
        score = 0
        WORD_SCORES[word] = score
        for c in word:
            score += FREQ_DICT[c]
        WORD_SCORES[word] = score

def pwords(sort_by_freq = False, qty=None):
    global WORDS, WORD_SCORES
    if sort_by_freq:
        make_word_scores()
        i = 0
        for k, v in sorted(WORD_SCORES.items(), key=lambda p:p[1], reverse=True):
            print(k, v)
            i += 1
            if qty and i >= qty:
                return
        return
    for word in WORDS:
        print(word)

if __name__ == '__main__':
    load_file()
