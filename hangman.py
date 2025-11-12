from words import get_random_word, display_hangman
from game_logic import HangmanGame


def main():
    print("=== ИГРА ВИСЕЛИЦА ===")
    print("Угадайте слово по буквам! Можно ошибиться 6 раз.")

    while True:
        # Начало игры
        word = get_random_word()
        game = HangmanGame(word)

        # Игровой процесс
        while game.is_playing():
            print(f"\n{display_hangman(game.mistakes)}")
            print(f"Слово: {game.get_hidden_word()}")
            print(f"Ошибки: {game.mistakes}/6")
            print(f"Использованные буквы: {', '.join(sorted(game.used_letters))}")

            letter = input("Введите букву: ").lower()

            if len(letter) != 1 or not letter.isalpha():
                print("❌ Введите одну букву!")
                continue

            game.guess_letter(letter)

        # Результат игры
        print(f"\n{display_hangman(game.mistakes)}")
        if game.is_won():
            print(f"🎉 ПОБЕДА! Слово: {word}")
        else:
            print(f"💀 ПРОИГРЫШ! Слово: {word}")

        # Повтор игры
        again = input("\nСыграем еще? (д/н): ").lower()
        if again != 'д':
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    main()
