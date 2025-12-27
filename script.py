import msvcrt
import config
import random
import os
import sys
import time

"""Debug setup"""
DEBUG = False


class ControlsBase:
    """[E] Вперед ↘ | [Q] Назад ↗ | [F] Выбрать ↱"""

    def __init__(self):
        pass


class AnimatedIntro:
    """Анимированная заставка для Wordle игры"""

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def typewriter_effect(text, delay=0.05):
        """Эффект печатной машинки"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    @staticmethod
    def run_intro(total_duration=5.0):
        """Запуск анимированной заставки с плавным появлением заголовка"""
        AnimatedIntro.clear_screen()

        print("\n" * 2)

        # Получаем заголовок для анимации
        title = """                                          
       ...   .     ...                               ..             ..            
  .~`"888x.!**h.-``888h.                             dF         x .d88"             
 dX   `8888   :X   48888>         u.      .u    .   '88bu.       5888R              
'888x  8888  X88.  '8888>   ...ue888b   .d88B :@8c  '*88888bu    '888R        .u    
'88888 8888X:8888:   )?""`  888R Y888r ="8888f8888r   ^"*8888N    888R     ud8888.  
 `8888>8888 '88888>.88h.    888R I888>   4888>'88"   beWE "888L   888R   :888'8888. 
   `8" 888f  `8888>X88888.  888R I888>   4888> '     888E  888E   888R   d888 '88%" 
  -~` '8%"     88" `88888X  888R I888>   4888>       888E  888E   888R   8888.+"    
  .H888n.      XHn.  `*88! u8888cJ888   .d888L .+    888E  888F   888R   8888L      
 :88888888x..x88888X.  `!   "*888*P"    ^"8888*"    .888N..888   .888B . '8888c. .+ 
 f  ^%888888% `*88888nx"      'Y"          "Y"       `"888*""    ^*888%   "88888%   
      `"**"`    `"**""                                  ""         "%       "YP'    """

        # Разбиваем заголовок на строки
        lines = title.strip('\n').split('\n')

        # Находим максимальную длину строки для анимации
        max_len = max(len(line) for line in lines)

        # Желтый цвет для всей анимации
        print("\033[33m")  # Желтый цвет

        # Анимация появления слева направо
        for i in range(max_len + 1):
            # Очищаем и перерисовываем
            AnimatedIntro.clear_screen()
            print("\n" * 2)  # Отступ сверху

            # Выводим видимую часть каждой строки
            for line in lines:
                visible_part = line[:i] if i <= len(line) else line
                print(visible_part)

            # Пауза для плавности
            time.sleep(0.02)

        print("\033[0m")  # Сброс цвета

        # Пауза после появления заголовка
        time.sleep(0.5)

        # Появление надписи WORDLE под заголовком
        print("\n" + " " * 35, end='')

        word = "Creator - Arnne1"

        # Появление каждой буквы с задержкой
        for i, letter in enumerate(word):
            # Задержка перед каждой буквой
            time.sleep(0.15)

            # Желтый цвет для всех букв
            print(f"\033[33m{letter}\033[0m", end='', flush=True)

            # Легкий эффект выделения буквы
            time.sleep(0.05)
            print(f"\b\033[93m{letter}\033[0m", end='', flush=True)  # Ярко-желтый
            time.sleep(0.05)
            print(f"\b\033[33m{letter}\033[0m", end='', flush=True)  # Возврат к обычному желтому

        print()
        time.sleep(0.5)
        AnimatedIntro.clear_screen()


"""Стилизация проекта"""


class Styling:
    @staticmethod
    def title():
        print(f"""                                          
       ...   .     ...                               ..             ..            
  .~`"888x.!**h.-``888h.                             dF         x .d88"             
 dX   `8888   :X   48888>         u.      .u    .   '88bu.       5888R              
'888x  8888  X88.  '8888>   ...ue888b   .d88B :@8c  '*88888bu    '888R        .u    
'88888 8888X:8888:   )?""`  888R Y888r ="8888f8888r   ^"*8888N    888R     ud8888.  
 `8888>8888 '88888>.88h.    888R I888>   4888>'88"   beWE "888L   888R   :888'8888. 
   `8" 888f  `8888>X88888.  888R I888>   4888> '     888E  888E   888R   d888 '88%" 
  -~` '8%"     88" `88888X  888R I888>   4888>       888E  888E   888R   8888.+"    
  .H888n.      XHn.  `*88! u8888cJ888   .d888L .+    888E  888F   888R   8888L      
 :88888888x..x88888X.  `!   "*888*P"    ^"8888*"    .888N..888   .888B . '8888c. .+ 
 f  ^%888888% `*88888nx"      'Y"          "Y"       `"888*""    ^*888%   "88888%   
      `"**"`    `"**""                                  ""         "%       "YP'    
""")

    @staticmethod
    def error(text):
        print(f"\033[33mПроизошла ошибка\033[0m: {text}")
        input("Нажмите любую клавишу чтобы продолжить...")

    @staticmethod
    def mainmenu(mark1: str, mark2: str, mark3: str):
        print(f"""
           [{mark1}] | Играть ↘
           [{mark2}] | Настройки ↘
           [{mark3}] | Выход ↺

           [E] \033[33mВперед ↘\033[0m | [Q] \033[33mНазад ↗\033[0m | [F] \033[33mВыбрать ↱\033[0m """)

    @staticmethod
    def settings(mark1: str, mark2: str, mark3: str):
        print(f"""
            [{mark1}] | Язык игры ↘
            [{mark2}] | Уровень языка ↘
            [{mark3}] | Управление ↘

            [ESC] | Назад ↺

            [E] \033[33mВперед ↘\033[0m | [Q] \033[33mНазад ↗\033[0m | [F] \033[33mВыбрать ↱\033[0m
""")


class Game:
    """Введение основных аргументов класса Game"""

    def __init__(self, styling):
        self.styling = styling
        self.Red = '\033[31m'
        self.Gre = '\033[32m'
        self.Yel = '\033[33m'
        self.Res = '\033[0m'
        self.word = []
        self.original_word = ""

    """тест config файла"""

    def get_random_word(self):
        try:
            if not hasattr(config, 'words') or len(config.words) == 0:
                raise ValueError("Список слов в config пуст или отсутствует")
            word_str = random.choice(config.words)
            self.original_word = word_str
            self.word = [char for char in word_str]
        except Exception as e:
            os.system('cls||clear')
            self.styling.error(e)
            return False
        return True

    def wordly(self):
        try:
            attempts = 0
            max_attempts = 6

            while attempts < max_attempts:
                os.system('cls||clear')
                self.styling.title()
                print(f"Попытка {attempts + 1}/{max_attempts}")
                print("Слово содержит", len(self.word), "букв")

                guess = input("Введите ваш вариант: ").lower().strip()

                if len(guess) != len(self.word):
                    print(f"Слово должно содержать {len(self.word)} букв. Попробуйте снова.")
                    input("Нажмите любую клавишу чтобы продолжить...")
                    continue

                user_word = [char for char in guess]
                result = []
                word_copy = self.word.copy()

                for i in range(len(self.word)):
                    if user_word[i] == self.word[i]:
                        result.append(f"{self.Gre}{user_word[i]}{self.Res}")
                        word_copy[i] = None
                    else:
                        result.append("_")

                for i in range(len(self.word)):
                    if result[i].startswith(self.Gre):
                        continue
                    if user_word[i] in word_copy:
                        result[i] = f"{self.Yel}{user_word[i]}{self.Res}"
                        idx = word_copy.index(user_word[i])
                        word_copy[idx] = None
                    else:
                        result[i] = f"{self.Red}{user_word[i]}{self.Res}"

                print("".join(result))
                attempts += 1

                if user_word == self.word:
                    print(f"Вы угадали слово за {attempts} попыток!")
                    input("Нажмите любую клавишу чтобы продолжить...")
                    return

                input("Нажмите любую клавишу чтобы продолжить...")

            print(f"Вы исчерпали все попытки. Загаданное слово: {''.join(self.word)}")
            input("Нажмите любую клавишу чтобы продолжить...")

        except Exception as e:
            os.system('cls||clear')
            self.styling.error(e)
            input("Нажмите любую клавишу чтобы продолжить...")

    def controls(self):
        os.system('cls||clear')
        print("Настройка управления")
        input("Нажмите любую клавишу чтобы продолжить...")
        pass

    """Настройки и выпадающие меню"""

    def settings_menu(self):
        current_selection = 0
        menu_items = 3

        while True:
            os.system('cls||clear')
            self.styling.title()

            marks = [' ', ' ', ' ']
            marks[current_selection] = '>'
            self.styling.settings(marks[0], marks[1], marks[2])

            key = msvcrt.getch()
            if DEBUG:
                print(f"{self.Yel}debug! key pressed:{self.Res} {key}")

            if key.lower() == b'e' or key == b'\xe3':
                current_selection = (current_selection + 1) % menu_items
            elif key.lower() == b'q' or key == b'\xa9':
                current_selection = (current_selection - 1) % menu_items
            elif key.lower() == b'f' or key == b'\xa0':
                if current_selection == 0:
                    os.system('cls||clear')
                    print("Настройка языка игры")
                    input("Нажмите любую клавишу чтобы продолжить...")
                elif current_selection == 1:
                    os.system('cls||clear')
                    print("Настройка уровня языка")
                    input("Нажмите любую клавишу чтобы продолжить...")
                elif current_selection == 2:
                    self.controls()
            elif key == b'\x1b':  # ESC для выхода из настроек
                break

    def mainloop(self):
        current_selection = 0
        menu_items = 3

        while True:
            os.system('cls||clear')
            self.styling.title()

            marks = [' ', ' ', ' ']
            marks[current_selection] = '>'
            self.styling.mainmenu(marks[0], marks[1], marks[2])

            key = msvcrt.getch()
            if DEBUG:
                print(f"{self.Yel}debug! key pressed:{self.Res} {key}")

            if key.lower() == b'e' or key == b'\xe3':
                current_selection = (current_selection + 1) % menu_items
            elif key.lower() == b'q' or key == b'\xa9':
                current_selection = (current_selection - 1) % menu_items
            elif key.lower() == b'f' or key == b'\xa0':
                if current_selection == 0:
                    while True:
                        os.system('cls||clear')
                        self.styling.title()
                        print(
                            "             [!] | Выберите режим игры: \n             [Q] | Случайное слово\n             [E] | Пользовательское слово\n\n             [F] | Назад")
                        key = msvcrt.getch()
                        if DEBUG:
                            print(f"{self.Yel}debug! key pressed:{self.Res} {key}")

                        if key == b'q':
                            if self.get_random_word():
                                self.wordly()
                            break
                        elif key == b'e':
                            while True:
                                os.system('cls||clear')
                                custom_word = input(
                                    f"Введите ваше слово, {self.Red}длиной в 5 букв!{self.Res}: ").lower().strip()
                                if custom_word.isalpha() and len(custom_word) == 5:
                                    self.original_word = custom_word
                                    self.word = [char for char in custom_word]
                                    self.wordly()
                                    break
                                else:
                                    print(
                                        f"[!] Слово должно быть 5 букв и содержать только буквы. Вы ввели {len(custom_word)} символов.")
                                    input("Нажмите любую клавишу чтобы продолжить...")
                            break
                        elif key == b'f':
                            break
                elif current_selection == 1:
                    self.settings_menu()
                elif current_selection == 2:
                    os.system('cls||clear')
                    print("Выход из игры...")
                    sys.exit(0)


if __name__ == '__main__':
    try:
        # Сначала показываем анимированную заставку
        AnimatedIntro.run_intro()

        # Затем запускаем игру
        game = Game(Styling)
        game.mainloop()

    except KeyboardInterrupt:
        os.system('cls||clear')
        print("Игра завершена.")
        sys.exit(0)