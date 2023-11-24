import random
import sys


class Hangman:
    def __init__(self):
        self.board = []
        self.lives = 6
        self.words = ['apple','banana','mango','lichi','dragonfruit','lehsun']
        self.winword = ''
    def main(self):
        start = input('start? Y/N').lower()
        if start == 'y':
            self.winword = random.choice(self.words).lower()
            self.setup()
            self.play()
        else:
            sys.exit('exit')

    def setup(self):
        for i in self.winword:
            self.board.append('_')
    def play(self):
        guessed = []
        while self.lives > 0:
            print(self.winword)
            letter = input('guess a letter')
            if letter in self.winword and letter not in guessed:
                guessed.append(letter)
                self.refreshboard(letter)
                self.checkwin()
            elif letter in guessed:
                print('letter already guessed')
            else:
                guessed.append(letter)
                print(f'{letter} does not exist in winword')
                self.lives -=1
            print(self.board)
        print(f'OUt OF LivEs.. WORD = {self.winword}')
    def refreshboard(self,letter):
        for i,ch in enumerate(self.winword):
            if letter == ch:
                self.board[i] = letter

    def checkwin(self):
        board_str = ''.join([str(ch) for ch in self.board])
        if board_str == self.winword:
            print(f"CONGRaTuLatiOns YOu WoN {self.winword} was the word")

            sys.exit()

new_game = Hangman()
new_game.main()