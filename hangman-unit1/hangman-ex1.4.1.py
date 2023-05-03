import random

print("\033[34mWelcome to the game Hangman")

print("\033[34m", ''' _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/''')
					
print("\033[34m", random.randint(5, 10), "\033[0m") # print an integer indicating how many (failed)
# guessing attempts a player is allowed in the game.