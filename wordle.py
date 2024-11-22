class Wordle:
    def __init__(self):
        self.wordle = "Block"
        self.wordle_map = set(self.wordle)
        #using ascii escape codes
        self.wordle_colors = {
            "red" : '\033[31m',
            "green" : '\033[32m',
            "yellow" : '\033[33m'
        }

    #main functionality to start game and repeat 
    def start_game(self):
        guess = ""

        while len(guess) != 5:
            guess = input("Enter your guess:")
            
        for index, char in enumerate(guess):
            if self.green_check(char, index):
                self.print_letter(char, "green")
            elif self.yellow_check(char):
                self.print_letter(char, "yellow")
            else:
                self.print_letter(char, "red")

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
    
    #print a box containing the letter in the appropirate color
    def print_letter(self, letter, color):
        color_code = self.wordle_colors[color]
        #all codes end wrapping in \033[0m
        print(f"{color_code}*\033[0m" * 7)
        print(f"{color_code}*\033[0m" * 2, end = "")
        print(f"{color_code} {letter} \033[0m", end = "")
        print(f"{color_code}*\033[0m" * 2)
        print(f"{color_code}*\033[0m" * 7)

        #prints a single box like this

        # *******
        # ** H **
        # *******

        
        

        
        
    

