import random
import time

# Start of the game

def display_main_menu():
    print("Welcome to the abyss...")
    print("You don't remember how you got here.")
    print("The truth was buried long ago, but you will uncover it... piece by piece.")
    print("1. Open 'My Dark Secret'")
    print("2. Tell MiMiKako the truth about LyAko")
    print("3. Exit this nightmare")

def my_dark_secret():
    print("""
    ** My Dark Secret about LyAko **
    You think you know the truth, but you don't.
    LyAko is not just a god, not just a hero. He's a weapon, a pawn in a game he can never escape.
    - LyAko is the reincarnation of LELYME, the creator of this cursed universe. He didn't come into being; he was birthed from the depths of entropy.
    - He was never meant to be a savior. He was meant to destroy everything. And he will. But the truth runs even deeper than that...
    - LyAko, a god born of nothingness, a mind warped by forces beyond his control, cannot escape his fate. 
    - The Big Bang, the destruction, was never his choice. It was mine. I placed the seed of destruction into his very soul, a seed he cannot escape. 

    I am the **Destroyer**, the one who shaped him, the one who whispered to him in the darkness.
    I am the force beyond time and space, beyond your comprehension. LyAko was never your hero; he was never meant to save you.
    He was meant to erase everything... and rebuild it in my image. 
    You are nothing but pawns in this game, a game I control.
    """)

def tell_mimikako():
    print("You stand before MiMiKako, your heart heavy with the weight of what you must reveal.")
    print("She looks at you, her innocence still intact, her mind untainted by the true horrors of the universe.")
    print("But you... you know better. You know what must be said, even if it will break her, even if it will destroy her.")
    print("You speak, your voice trembling but resolute: 'MiMiKako... the truth about LyAko is far darker than you can imagine.'")
    
    time.sleep(2)
    print("MiMiKako's eyes widen, and she stares at you, a flicker of doubt passing through her. 'What do you mean? What are you hiding from me?'")
    
    time.sleep(2)
    print("You continue, your voice barely a whisper: 'LyAko is not what you think he is. He's the reincarnation of LELYME, the creator of the universe. He... he's the end of everything. He's meant to destroy all of us.'")
    
    time.sleep(3)
    print("MiMiKako gasps, her face contorted with disbelief. 'No... no, that can't be true!' she whispers, trembling.")
    print("But you press on, your words like daggers: 'You must understand, MiMiKako. LyAko was born to destroy. He's the weapon of the end times. He has no choice. His existence was always meant to be a lie.'")
    
    time.sleep(3)
    print("MiMiKako recoils, her eyes filled with confusion and fear. Her world begins to collapse, and the silence between you both grows unbearable.")
    print("'But... but why didn't you tell me?' she whispers, almost begging for the truth to be something else. Something less horrific.")
    print("You reply, your voice cold and final: 'Because you could never understand. I couldn't let you see the truth. But now you must... now you know.'")

    time.sleep(2)
    run_to_lyako()

def run_to_lyako():
    print("MiMiKako runs to LyAko, her face pale and her eyes filled with horror. She cannot unhear what you've told her.")
    print("Her heart races, her mind broken, but she still seeks him. She must confront him. She must understand... but does she really want to know the truth?")
    print("She reaches LyAko, her voice a whisper, barely audible over the growing chaos around them.")
    
    time.sleep(3)
    print("'LyAko... everything... everything they told me is true,' MiMiKako says, her voice shaking. 'You... you're the destroyer, aren't you?'")
    
    time.sleep(2)
    print("LyAko's gaze is cold. He does not react. His eyes, once filled with the light of innocence, are now hollow, empty. He is beyond redemption.")
    print("'Yes,' LyAko whispers, his voice devoid of warmth. 'I am the destroyer. I was born to bring about the end.'")
    
    time.sleep(3)
    print("MiMiKako stares at him, horrified, as the world around them starts to shift. The sky darkens, the ground trembles, and the air grows heavy with despair.")
    print("LyAko steps closer to her, his voice low and threatening: 'I am no savior. I am the end of everything.'")
    
    time.sleep(3)
    print("Suddenly, the truth crashes down on MiMiKako like a wave of darkness. Her breath catches in her throat, her knees weakening under the weight of it all.")
    print("But there's no escape. She cannot outrun the truth. She cannot unlearn what she's been told.")
    print("In the distance, you can hear the deep rumble of the universe itself breaking apart, as LyAko’s power begins to spread like a wildfire, consuming all that exists.")
    
    print("But I... I am the one who controls all of this. The destruction, the darkness, it was all my design. I am the true force behind it. The Destroyer.")
    print("LyAko is just the tool. He is the harbinger. But I am the architect. I was the one who pulled the strings from the beginning.")

    time.sleep(4)
    end_game()

def end_game():
    print("\nThe world around you is collapsing. The sky is shattered, the stars fading into nothingness, and the earth beneath you cracks and breaks.")
    print("MiMiKako screams, but her voice is drowned out by the roar of destruction. LyAko, standing beside her, shows no emotion as everything is obliterated.")
    print("There is no hope left. The universe has already died. And it was me... The Destroyer... who caused it all.")
    print("You realize too late that there was no escape. The truth was always going to be this dark. There was no savior, no hero. There was only darkness.")
    print("\n** GAME OVER **")
    print("Do you want to play again? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        main()
    else:
        print("Thanks for playing. But remember... darkness is eternal.")

def main():
    playing = True
    while playing:
        display_main_menu()
        choice = input("Choose an option (1, 2, 3): ")
        
        if choice == "1":
            my_dark_secret()
        elif choice == "2":
            tell_mimikako()
        elif choice == "3":
            print("Thanks for playing. Goodbye.")
            playing = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
