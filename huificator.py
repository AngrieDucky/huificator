class Huificator():
    """
    Huify a single word. Because why not?
    """
    def __init__(self) -> None:
        self._vowels = ["а", "о", "е", "ю", "и", "у", "ы", "я", "ё", "э"]
        self._exchange = {"а": "я", "о": "ё", "у": "ю", "ы": "и"}

    def is_word(self, word: str) -> bool:
        if word.isalpha():
            return True
        return False
    
    def is_changeable(self, letter: str) -> bool:
        if letter in self._exchange.keys():
            return True
        return False
    
    def change_letter(self, letter: str) -> str:
        return self._exchange[letter].value()

    def huify(self, word: str) -> str:
        if not self.is_word(word):
            return "Хуёв тачку, ага. Одно слово передавай, блять!"
        word = word.lower()
        final_word = word
        for i in word:
            if (i in self._vowels) and self.is_changeable(i):
                i = self.change_letter(i)
                return "ху"+final_word
            elif (i in self._vowels) and not self.is_changeable(i):
                return "ху"+final_word
            else:
                final_word = word[word.index(i)+1:]
