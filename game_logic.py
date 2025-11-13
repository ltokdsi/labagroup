class HangmanGame:
    def __init__(self, word):
        self.word = word.lower()
        self.hidden_word = ['_'] * len(word)
        self.used_letters = set()
        self.mistakes = 0
        self.max_mistakes = 6

    def guess_letter(self, letter):
        """Проверяет букву и обновляет состояние игры"""
        if letter in self.used_letters:
            print("❌ Эта буква уже была!")
            return

        self.used_letters.add(letter)

        if letter in self.word:
            # Буква угадана - открываем её в слове
            for i, char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i] = letter
            print("✅ Верно!")
        else:
            # Неверная буква
            self.mistakes += 1
            print("❌ Нет такой буквы!")

    def get_hidden_word(self):
        """Возвращает текущее состояние угадываемого слова"""
        return ' '.join(self.hidden_word)

    def is_playing(self):
        """Проверяет, продолжается ли игра"""
        return not self.is_won() and not self.is_lost()

    def is_won(self):
        """Проверяет, выиграл ли игрок"""
        return '_' not in self.hidden_word

    def is_lost(self):
        """Проверяет, проиграл ли игрок"""
        return self.mistakes >= self.max_mistakes