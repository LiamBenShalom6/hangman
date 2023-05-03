HANGMAN_ASCII_ART = "\033[34mWelcome to the game Hangman" + "\n" + ('''  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/''')
					 
MAX_TRIES = 6

print(HANGMAN_ASCII_ART, "\n" + str(MAX_TRIES), "\033[0m")