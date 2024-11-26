class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                content = file.read().lower()
                for punct in punctuations:
                    content = content.replace(punct, '')
                words = content.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            position = words.index(word) + 1
            result[name] = position
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result
    
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего

