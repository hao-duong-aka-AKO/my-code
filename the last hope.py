import time
import random

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def slow_input(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()

slow_print("Welcome to the last part of the phone simulator")
password = slow_input("pL34$3 3Nt3r 4 p4$$w0rD: ")
player_name = slow_input("Wh4t 1$ Y0Ur N4m3: ")

slow_print("LeAgosal: h3lp u$.")
slow_print("MiMikako: Are you from another world?")
slow_print(f"{player_name} (Elements battle): Actually, we are from another universe. And we will help you.")
slow_print(f"{player_name} (all): He is right, we will help you!")
slow_print("The Destroyer: you will regret this !-!")

# Battle setup
if player_name.upper() == "LELYME":
    player_hp = float('inf')  # Immortal mode
    slow_print("You are LELYME... the original creator. Death cannot touch you.", 0.05)
else:
    player_hp = 500

destroyer_hp = 400

slow_print("The battle begins...", 0.05)

# Battle loop
while player_hp > 0 and destroyer_hp > 0:
    slow_print(f"\n{player_name} HP: {'∞' if player_hp == float('inf') else player_hp} | The Destroyer HP: {destroyer_hp}", 0.03)
    action = input("Choose your action - (A)ttack or (D)odge: ").upper()
    enemy_action = random.choice(["ATTACK", "DODGE"])

    player_damage = random.randint(150, 190)
    destroyer_damage = random.randint(145, 200)

    # Critical chance
    if random.randint(1, 5) == 5:
        player_damage += 100
        slow_print("Critical Hit!", 0.03)

    if action == "A":
        if enemy_action == "ATTACK":
            destroyer_hp -= player_damage
            if player_hp != float('inf'):
                player_hp -= destroyer_damage
            slow_print(f"You dealt {player_damage} damage.", 0.03)
            slow_print(f"The Destroyer dealt {destroyer_damage} damage.", 0.03)
        elif enemy_action == "DODGE":
            slow_print("Your attack missed! The Destroyer dodged it.", 0.03)
    elif action == "D":
        if enemy_action == "ATTACK":
            slow_print("You dodged The Destroyer's attack!", 0.03)
        else:
            slow_print("Both of you dodged. Nothing happened.", 0.03)

# End of battle
if destroyer_hp <= 0:
    slow_print("\nYou defeated The Destroyer. The corruption has ended.", 0.05)
    if player_name.upper() == "LELYME":
        slow_print("As LELYME, you now decide the fate of all existence...", 0.07)
    else:
        slow_print("Hope has been restored. You are the new light of this universe.", 0.07)
else:
    slow_print("\nYou were defeated... The universe falls into darkness...", 0.07)
