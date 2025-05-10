# Simple text-based game about Ako and Mikako's love story

import time

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("Welcome to the story of Ako and Mikako!")
    slow_print("This is a game about choices, love, and emotion.")
    slow_print("Will Ako open up to Mikako, or will he remain distant?")
    slow_print("Let's begin...\n")

def birthday_scene():
    slow_print("It is Mikako's birthday today, and Ako is about to wish her well.")
    slow_print("Ako: 'Happy birthday, Mikako.'")
    slow_print("Mikako looks at Ako, her expression softens... she has something on her mind.")
    slow_print("Mikako: 'Thank you, Ako. But... there's something I need to do.'")
    slow_print("Mikako suddenly kisses Ako. His face turns red, but he tries to stay calm.\n")
    
def decision_point():
    slow_print("Mikako looks at Ako, waiting for his response. Will he push her away or embrace the moment?")
    
    choice = input("What will Ako do? (1) Push her away (2) Stay calm and say nothing: ")
    
    if choice == "1":
        slow_print("Ako pushes Mikako gently away. He stays silent, his expression unreadable.")
        slow_print("Mikako feels the sting of rejection but doesn't give up. She knows Ako's true feelings.")
        slow_print("Mikako: 'I won't give up on you, Ako.'")
        slow_print("Everyone shocked")
        ending()
    
    elif choice == "2":
        slow_print("Ako stays calm, his face betraying no emotion. Mikako waits nervously for his reaction.")
        slow_print("Ako: '...Why did you do that?'")
        slow_print("Mikako smiles softly: 'Because I love you, Ako.'")
        slow_print("Ako remains silent, but something inside him begins to stir. Can he open his heart?\n")
        slow_print("Everyone shocked")
        ending()
    
    else:
        slow_print("That's not a valid option. Try again.\n")
        decision_point()

def ending():
    slow_print("The story continues... but where will it lead?")
    slow_print("The choice is yours, and their love story has just begun.")
    slow_print("To be continued...\n")

def main():
    intro()
    birthday_scene()
    decision_point()

# Start the game
main()
