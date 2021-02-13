import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if get_guessed_word(secret_word, letters_guessed) == secret_word:
     return True 
    else:
      return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word = guessed_word + secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letter= string.ascii_lowercase
    letters_left = " "
    for i in letter:
      if i not in letters_guessed:
        letters_left+=i
    return(letters_left)

def get_hint(secret_word,letters_guessed):
  import random
  letters_not_gussed = []
  i = 0
  while i < len(secret_word):
    if i not in letters_not_gussed :
      letters_not_gussed.append(secret_word[i])
    i = i +1
  return random.choice(letters_not_gussed)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print ("Welcome to the game, Hangman!")
    print( "I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    # print(secret_word)
    Difficulty_level = input("select your difficulty hard or medium or easy : ")
    if Difficulty_level == "easy":
      remaining_lives = 8
      images = [0,1,2,3,4,5,6,7]
    elif Difficulty_level == "medium":
      remaining_lives =  6
      images = [0,1,3,5,6,7]
    else:
      remaining_lives =  4
      images = [0,2,4,6]
    letters_guessed = []
    i = 0
    # remaining_lives = len(secret_word)
    while i < len(secret_word):
      available_letters = get_available_letters(letters_guessed)
     
      hint = input("do you want hint : ")
      if hint == "yes":
        print(get_hint(secret_word,letters_guessed))
      elif hint == "no":
        pass
      else:
        print("invalid hint")
        continue
      print("Available letters: " + available_letters)
      guess = input("Please guess a letter: ")
      if len(guess) == 1 and guess in available_letters:
        pass
      else:
        print("invalid guess please select one letter whatever you available ")
        continue
      letter = guess.lower()
      if letter in secret_word:
        letters_guessed.append(letter)
        print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        print ("")
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
          print (" * * Congratulations, you won! * * ")
          print ("")
          break
      else:
        print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
        letters_guessed.append(letter)
        print ("")
        images = 8-remaining_lives
        if images < 0:
          print(IMAGES[0])
        else:
          print(IMAGES[images])
    
        print("remaining lives",remaining_lives)
      remaining_lives = remaining_lives - 1
      i = i + 1  
        

    if secret_word != get_guessed_word(secret_word, letters_guessed):
      print("Sorry Game over you Didn't guessed the word,the word is",secret_word)
  # Load the list of words into the variable wordlist
  # So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)