import random

# Starting the second part of the game
choice = input("""
           TRIO DESTROYER: PART 2
             _________
            |         |
            |  Play > |
            |_________|
            Press e to continue
""")

if choice == "e":
    print("~~~Game Starting~~~")

# Continue from previous name and character choice
ur_name = input("Enter Your Name: ")

# Continue from Part 1: LyAko's adventure continues
print(f"{ur_name}, you are LyAko (main character).")
print("Your adventure continues, but the universe is glitching around you...")

# Strange occurrences happening, introducing new entities
print("Suddenly, a large rift appears in the sky, and the very fabric of space seems to tremble.")
print("A voice whispers in the wind: 'The end is near, but the beginning of destruction has arrived.'")

# Introducing the White Void and Black Void as allies
print("\nThe White Void speaks...")
print("White Void: 'I am the balance, the nothingness that allows creation. I am here to aid you, LyAko.'")
print("Black Void: 'I am the force of destruction, but also the will to preserve. Together, we must stop The Thing.'")

# Player remarks on White Void and Black Void looking familiar
print(f"\n{ur_name}: 'You two look familiar... Why do I feel like I've seen you before?'")
print("The White Void and Black Void exchange a glance, and a mysterious silence fills the air.")
print("White Void: 'You have seen us in your dreams, LyAko, in the spaces between time. We have always been with you.'")
print("Black Void: 'Our presence exists in the hidden corners of the universe, in the forgotten shadows of creation.'")

# Introducing the Quasi Holes and The Thing (True Form of Entity)
print("\nA massive Quasi Hole opens before you, an entity born from the collapsing universe.")
print("From the Quasi Hole emerges the true form of Entity, The Thing, a shifting mass of void and power.")
print("The Thing: 'I am the end of all. The universe will be consumed.'")

# Battle with The Thing begins
thing_health = 250  # The Thing's health increases in Part 2
thing_damage = random.choice([50, 60, 70])

# Player's initial health remains the same
ur_health = 250
battle_2 = True

while battle_2:
    print(f"\n{ur_name} Health: {ur_health} | The Thing Health: {thing_health}")

    action = input("Choose your action: (Attack/Heal): ").lower()

    if action == "attack":
        # Normal attack
        attack_chance = random.randint(1, 100)
        if attack_chance < 90:  # 90% chance for normal hit
            damage = random.choice([25, 35, 45])
            thing_health -= damage
            print(f"{ur_name} attacks The Thing, causing {damage} damage!")
        else:
            print(f"{ur_name}'s attack missed!")

    elif action == "heal":
        heal = random.randint(20, 40)
        ur_health += heal
        print(f"{ur_name} heals for {heal} health!")

    # The Thing's turn to attack
    if random.randint(1, 100) < 75:
        damage = thing_damage * 2  # Critical hit chance for The Thing
        print("The Thing lands a critical hit!")
    else:
        damage = thing_damage
    ur_health -= damage
    print(f"The Thing attacks {ur_name}, causing {damage} damage!")

    # Check if The Thing has been defeated
    if thing_health <= 0:
        print("You have defeated The Thing!")
        break

    # Check if the player is defeated
    if ur_health <= 0:
        print(f"{ur_name} has been defeated!")
        break

# If the battle ends, continue the story
if ur_health > 0:
    print(f"\n{ur_name}: 'This isn't over. There is more to uncover... What is the true purpose of these voids?'")
    print("Suddenly, you hear the voices of the White Void and Black Void once more.")

# The White Void speaks
print("\nWhite Void: 'You may have defeated The Thing, but the balance is broken. I cannot save you from the inevitable.'")

# The Black Void speaks
print("Black Void: 'Destruction cannot be undone. Prepare for what is to come.'")

# The world glitches and the player finds themselves in an unstable dimension
print("\nThe very ground beneath you cracks open, and you find yourself falling into an unknown dimension.")
print("A strange force surrounds you. It's like you're in-between the worlds—caught between creation and destruction.")

# Final twist - The entities' true nature revealed
print("\nThe White Void reveals the truth...")
print("White Void: 'I am not just an entity of creation, but also your ally. Together, we can stop the corruption of the universe.'")

print("\nThe Black Void laughs...")
print("Black Void: 'I am the void that devours, but I protect what is worthy. You are not alone in this fight.'")

# Ending for Part 2
print("\nThe game ends... but the adventure is far from over.")
print("You have barely scratched the surface of what lies ahead.")
print("End of Part 2")
