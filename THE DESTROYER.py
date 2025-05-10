import random

choice = input("""
           THE DESTROYER
             _________
            |         |
            |  Play > |
            |_________|
            Press e to play
""")

if choice == "e":
    print("~~~Game Starting~~~")

# Getting player name
ur_name = input("""
 ______________________
|                      |    0
|    Enter Your Name   |
|______________________|    0                 """)

# Choosing a character
ur_char = input(f"""{ur_name} chose a character:
\ ' /: LyAko(1 to chose)
- ' -: LeAgosal(2 to chose)
> ' <:Mekakas(3 to chose)               

""")

if ur_char == "1":
    print(f"{ur_name}, you are LyAko (main character)")
    print("Let's start your adventure")
    print("So, You are at the Amock village")
    print("You met Mekakas")
    talkos = input("Press e to talk").lower()
    if talkos == "e":
        print("Mekakas: Hi the weak one🤣🤣🤣")
        print(f"LyAko({ur_name}): Hello")
        print("Mekakas: You will never be strong🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣")
        print(f"LyAko({ur_name}): Really😑😑😑")
    else:
        print("You and him start a battle anyways")

print("You and Kakas start a battle")
ur_health = 250
kakas_health = 290
ur_dammage = random.choice([20, 30, 40])
ur_critical_hit = 90
kakas_dammage = random.choice([20, 30, 40])
kakas_critical_hit = 90
battle_1 = True

while battle_1:
    print(f"{ur_name} Health: {ur_health} | Kakas Health: {kakas_health}")

    # Battle actions
    action = input("Choose your action: (Attack/Heal): ").lower()

    if action == "attack":
        # Normal attack
        if random.randint(1, 100) < ur_critical_hit:
            damage = ur_dammage * 2
            print(f"{ur_name} lands a critical hit!")
        else:
            damage = ur_dammage
        kakas_health -= damage
        print(f"{ur_name} attacks Kakas, causing {damage} damage!")
    
    elif action == "heal":
        heal = random.randint(10, 20)
        ur_health += heal
        print(f"{ur_name} heals for {heal} health!")

    # Kakas' turn to attack
    if random.randint(1, 100) < kakas_critical_hit:
        damage = kakas_dammage * 2
        print("Kakas lands a critical hit!")
    else:
        damage = kakas_dammage
    ur_health -= damage
    print(f"Kakas attacks {ur_name}, causing {damage} damage!")

    # Check if anyone's health is below 100
    if ur_health < 200 or kakas_health < 200:
        print("Agosal enters the scene to stop the battle!")
        print("Agosal: Stop this! Both of you are too weak to continue!")
        break

    # Check if either character's health drops to zero or below
    if ur_health <= 0:
        print(f"{ur_name} has been defeated!")
        battle_1 = False
    elif kakas_health <= 0:
        print("Kakas has been defeated!")
        battle_1 = False

# If battle ended by Agosal or defeat, continue story
if ur_health > 0 and kakas_health > 0:
    print(f"Agosal: Both of you need to stop fighting, you are both strong!")
    print(f"{ur_name}: Thank you Agosal for stopping the battle!")

# EntityL3gg3st interference
print("Suddenly, a portal opens and Agosal gets infected by EntityL3gg3st!")

# Agosal's reaction
print("Agosal: NO! I am infected! EntityL3gg3st is taking control!")
print(f"{ur_name}: Agosal! We need to save you!")

# Battle against EntityL3gg3st
print("The battle against EntityL3gg3st begins!")

# Hypothetical battle with EntityL3gg3st (you can adjust this part as needed)
entity_health = 200
entity_damage = random.choice([30, 40, 50])

while entity_health > 0:
    action = input("Choose your action: (Attack/Heal): ").lower()

    if action == "attack":
        if random.randint(1, 100) < ur_critical_hit:
            damage = ur_dammage * 2
            print(f"{ur_name} lands a critical hit!")
        else:
            damage = ur_dammage
        entity_health -= damage
        print(f"{ur_name} attacks EntityL3gg3st, causing {damage} damage!")
    
    elif action == "heal":
        heal = random.randint(40, 50)
        ur_health += heal
        print(f"{ur_name} heals for {heal} health!")

    # EntityL3gg3st's turn to attack
    if random.randint(1, 100) < 80:
        damage = entity_damage/2
        print("EntityL3gg3st lands a critical hit!")
    else:
        damage = entity_damage
    ur_health -= damage
    print(f"EntityL3gg3st attacks {ur_name}, causing {damage} damage!")

    # Check if EntityL3gg3st has been defeated
    if entity_health <= 0:
        print("You have defeated EntityL3gg3st!")
        break

    # Check if the player is defeated
    if ur_health <= 0:
        print(f"{ur_name} has been defeated!")
        break

# Final victory message
if ur_health > 0:
    print(f"{ur_name}(trioeyes): We did it! Thanks, Agosal, Kakas and Mekakas!")
print("The game ends...easily like that?")
print("Everyone seems strange(exept you, Mekakas, Kakas, you(from trio eyes) and Agosal)")
print("End of part 1")