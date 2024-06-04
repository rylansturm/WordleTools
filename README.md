# WordleTools

I suppose this is my admission that I occasionally cheat at Wordle. But mostly this was just a fun, quick exercise with string and array manipulation in Python.

## Use

Currently I only have a few command line tools. I've thought about adding this to my server and having a webapp for it. We'll see.

Start by running Python in the command line.

```bash
$ python3
```

Then import the tools and load the words.

```python
from wordle import *
load_file()
```

The `load_file()` command does have an optional argument for a file name. If none is provided, the included `words.txt` will be loaded.
A global variable `WORDS` is now populated with the words from the file. You should not have to access that variable. The following 
commands are now available:

* `load_file(f = 'words.txt')`
    * Replaces `WORDS` with an array of words from the given file. The file must have one word per line.
* `remove_char(c)`
    * Removes all words in `WORDS` with the character `c`
* `set_char(c, i)`
    * Removes all words in `WORDS` that don't have character `c` at index `i` (1-based index, i.e. characters are at positions 1, 2, 3, 4, 5).
      All words that do not match this pattern will be removed from `WORDS`
* `pwords()`
    * Prints all words in `WORDS`
 
## Current workflow

The way I currently use this is when I can't think of a word that matches the pattern. Say I'm a few guesses in. I'll use today's puzzle (2024-06-04, answer 'groom') as an example.

```python
from wordle import *
load_file()

set_char('g', 1)
set_char('r', 2)
set_char('o', 3)

for c in ['w', 'e', 't', 'u', 'a', 's', 'c', 'n']:
  remove_char(c)

pwords()
```

output:

```
grody
groof
groom
grovy
```

Usually if you're a few words in and following a good strategy for eliminating characters this list will be pretty small. 

Have fun!
