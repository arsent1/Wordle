class Wordle:
    def __init__(self):
        self.wordle = "Block"
        self.wordle_map = set(self.wordle)

    #main functionality to start game and repeat 
    def start_game(self):
        guess = ""

        while len(guess) != 5:
            guess = input("Enter your guess:")
            
        for index, char in enumerate(guess):
            print(index, char)
            if self.green_check(char, index):
                print("Letter in correct spot")
            elif self.yellow_check(char):
                print("Letter in word")
            else:
                print("Letter not in word")

    #check if letter is incorrect spot
    def yellow_check(self, letter):
        if letter in self.wordle_map:
            return True
        return False
    
    #check if letter is in correct spot in Wordle
    def green_check(self, char, index):
        if char == self.wordle[index]:
            return True
        return False
    
    def print_guess(self, guess):
        print("*" * 27)
        for i in range(5):
            print("**", end = " ")
            print(guess[i], end = " ")
        print("**", end = " ")
        print("\n" + "*" * 27)
        

        
        
    

