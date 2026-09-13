class WordDictionary:

    def __init__(self):
        self.store = []

    def addWord(self, word: str) -> None:
        self.store.append(word)

    def search(self, word: str) -> bool:
        for w in self.store:
            if len(w) != len(word):
                continue
            
            i=0 
            while i < len(word):
                if word[i] == "." or word[i] == w[i]:
                    i += 1
                else:
                    break
            if i == len(w):
                return True
        return False