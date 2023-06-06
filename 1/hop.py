class HopGame:
    def __init__(self):
        self.game_number = 0

    # a function for clearing console
    def clear():
        import os

        os.system("cls")

    # a function for greeting the user and asking for his/her name and hop coefficient
    def greet(self):
        HopGame.clear()
        print("*** Hello, Welcome to Hop Game ***")
        print("\nPlease enter your name:")
        name = input()
        self.score_list = [name]
        self.user_score = 0

        HopGame.clear()
        print("Please enter a number for hop coefficient:")
        self.coefficient = int(input())

    # a function for generating a random number
    def random_number(self):
        import random

        while True:
            self.randomNumber = random.randint(1, 10)
            if self.randomNumber % self.coefficient != 0:
                break
        self.game_number = self.randomNumber
        HopGame.clear()
        print("The first number is: ", self.randomNumber)

    # a function for getting the user's input
    def user_input(self):
        print("Please enter the next number:")
        # checking if the user's input is a number or not
        self.user_number = input()
        if self.user_number == "hop":
            pass
        else:
            self.user_number = int(self.user_number)

    # computer's turn
    def computer_turn(self):
        self.game_number += 2
        if self.game_number % self.coefficient == 0:
            HopGame.clear()
            print("hop")
        else:
            HopGame.clear()
            print("The current number is:", self.game_number)

    # checking user's input
    def check_input(self):
        while True:
            if self.user_number == "hop":
                self.user_score += 1
                self.computer_turn()
            else:
                if self.user_number == self.game_number + 1:
                    if self.user_number % self.coefficient == 0:
                        HopGame.clear()
                        print("You lost!", end=" ")
                        break
                    else:
                        self.user_score += 1
                        self.computer_turn()
                else:
                    HopGame.clear()
                    print("You lost!", end=" ")
                    break

            self.user_input()
        print("Your score is:", self.user_score)
        self.score_list.append(self.user_score)

    # a function for asking the user if he/she wants to play again
    def play_again(self):
        self.check_score()
        print("\n=== Score Board ===")
        self.parse_all_scores()
        print("\nDo you want to play again? (y/n)")
        answer = input()
        if answer == "y":
            self.game_number = 0
            self.randomNumber = 0
            self.run()
        else:
            HopGame.clear()
            print("Goodbye!")

    # a function for parsing all scores
    def parse_all_scores(self):
        [print(i[0], ":", i[1]) for i in all_scores]

    def check_score(self):
        check = False
        for i in all_scores:
            if i[0] == self.score_list[0]:
                check = True
                if i[1] < self.score_list[1]:
                    i[1] = self.score_list[1]
                else:
                    pass
        if check == False:
            all_scores.append(self.score_list)

    # a function for running the game
    def run(self):
        self.greet()
        self.random_number()
        self.user_input()
        self.check_input()
        self.play_again()


if __name__ == "__main__":
    all_scores = []
    game = HopGame()
    game.run()
