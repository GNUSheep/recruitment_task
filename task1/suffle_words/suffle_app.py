from random import sample
from typing import List
import unicodedata
import string

# By doing this that way, I can seperate all the words not only by looking for whitespaces.
class Parser:
    def __init__(self):
        self.seperators = {chr(cp) for cp in range(0x110000) if unicodedata.category(chr(cp)) == 'Zs'}
        self.seperators.update(string.punctuation)

    def split(self, line: str) -> List[str]:
        words = []

        cur_word = ""
        for c in line:
            if c in self.seperators:
                words.append((cur_word, c))
                cur_word = ""
            else:
                cur_word += c

        if len(cur_word) != 0:
            words.append((cur_word, ""))

        return words

def suffle(file_content: str) -> str:
    shuffled_file = ""

    parser = Parser()
    
    for line in file_content.split("\n"):
        for word, sep in parser.split(line):
            # keeping out unnecessary shuffle
            if len(word) <= 3:
                shuffled_file += word + sep
                continue
            
            shuffled_word = sample(list(word[1:-1]), len(word[1:-1]))
            shuffled_file += word[0] + ''.join(shuffled_word) + word[-1] + sep
        shuffled_file += "\n"
    return shuffled_file
